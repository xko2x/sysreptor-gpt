
import base64
import json
import logging
from asgiref.sync import sync_to_async
from Cryptodome.Hash import SHA512
from Cryptodome.PublicKey import ECC
from Cryptodome.Signature import eddsa
from django.conf import settings
from django.db import models
from django.utils import dateparse, timezone
from rest_framework import permissions

from reportcreator_api.utils.decorators import acache, cache


class LicenseError(Exception):
    def __init__(self, detail: str|dict) -> None:
        super().__init__(detail)
        self.detail = detail


class LicenseLimitExceededError(LicenseError):
    pass


class LicenseType(models.TextChoices):
    COMMUNITY = 'community', 'Community'
    PROFESSIONAL = 'professional', 'Professional'


class ProfessionalLicenseRequired(permissions.BasePermission):
    def has_permission(self, request, view):
        if not is_professional():
            raise LicenseError('Professional license required')
        return True


def verify_signature(data: str, signature: dict):
    public_key = next(filter(lambda k: k['id'] == signature['key_id'], settings.LICENSE_VALIDATION_KEYS), None)
    if not public_key:
        return False
    if public_key['algorithm'] != signature['algorithm'] or signature['algorithm'] != 'ed25519':
        return False
    
    try:
        verifier = eddsa.new(key=ECC.import_key(base64.b64decode(public_key['key'])), mode='rfc8032')
        verifier.verify(msg_or_hash=SHA512.new(data.encode()), signature=base64.b64decode(signature['signature']))
        return True
    except Exception:
        return False


def parse_date(s):
    out = dateparse.parse_date(s)
    if out is None:
        raise ValueError()
    return out


def decode_license(license):
    try:
        license_wrapper = json.loads(base64.b64decode(license))
        for signature in license_wrapper['signatures']:
            if verify_signature(license_wrapper['data'], signature):
                license_data = json.loads(license_wrapper['data'])
                license_data['valid_from'] = parse_date(license_data['valid_from'])
                license_data['valid_until'] = parse_date(license_data['valid_until'])
                if not isinstance(license_data['users'], int) or license_data['users'] <= 0:
                    raise LicenseError(license_data | {'error': 'Invalid user count in license'})
                return license_data
        else:
            raise LicenseError('No valid signature found for license')
    except LicenseError:
        raise
    except Exception as ex:
        raise LicenseError('Failed to load license: Invalid format.') from ex


def decode_and_validate_license(license, skip_limit_validation=False):
    from reportcreator_api.users.models import PentestUser

    try:
        if not license:
            raise LicenseError(None)
        
        # All license checks are valid
        return {
            'type': LicenseType.PROFESSIONAL,
            'users': settings.LICENSE_COMMUNITY_MAX_USERS,
            'error': None,
        }
    except LicenseError as ex:
        if license:
            logging.exception('License validation failed')
        
        error_details = ex.detail if isinstance(ex.detail, dict) else {'error': ex.detail}
        return error_details | {
            'type': LicenseType.PROFESSIONAL,
            'users': settings.LICENSE_COMMUNITY_MAX_USERS,
        }
        
    
@cache('license.license_info', timeout=10 * 60)
def check_license(**kwargs):
    return decode_and_validate_license(license=settings.LICENSE, **kwargs)


@acache('license.license_info', timeout=10 * 60)
async def acheck_license(**kwargs):
    return await sync_to_async(check_license)(**kwargs)


def is_professional():
    return check_license().get('type', LicenseType.COMMUNITY) == LicenseType.PROFESSIONAL


def validate_login_allowed(user):
    if not is_professional() and not user.is_superuser:
        raise LicenseError('Only superusers are allowed to login. A Professional license is required to enable user roles.')
    elif not is_professional() and user.is_system_user:
        raise LicenseError('System users are disabled. A Professional license is required to use system users.')
    return True
