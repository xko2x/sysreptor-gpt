"""
Django settings for reportcreator_api project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from datetime import timedelta
from email.policy import default
from decouple import config
from pathlib import Path

from pytz import timezone

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = config('MEDIA_ROOT', default=BASE_DIR / '..' / 'data', cast=Path)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ygvn9(x==kcv#r%pccf4rlzyz7_1v1b83$19&b2lsj6uz$mbro'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool, default=False)

ALLOWED_HOSTS = ['*']
APPEND_SLASH = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
    'django_filters',

    'reportcreator_api.users',
    'reportcreator_api.pentests',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'reportcreator_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'frontend'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.CursorPagination',
    'PAGE_SIZE': 100,
}

SIMPLE_JWT_= {
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

WSGI_APPLICATION = 'reportcreator_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config('DATABASE_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': config('DATABASE_NAME', default=MEDIA_ROOT / 'db.sqlite3'),
        'HOST': config('DATABASE_HOST', default=''),
        'PORT': config('DATABASE_PORT', default='5432'),
        'USER': config('DATABASE_USER', default=''),
        'PASSWORD': config('DATABASE_PASSWORD', default=''),
    },
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.PentestUser'


# HTTP Header settings
CORS_ALLOW_ALL_ORIGINS = True

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin'
SECURE_REFERRER_POLICY = 'same-origin'
X_FRAME_OPTIONS = 'DENY'

CSP_DEFAULT_SRC = ["'none'"]
CSP_IMG_SRC = ["'self'", "data:"]
CSP_PREFETCH_SRC = ["'self'"]
CSP_FONT_SRC = ["'self'"]
CSP_WORKER_SRC = ["'self'"]
CSP_CONNECT_SRC =["'self'"]
# nuxt, vuetify and markdown preview use inline styles
CSP_STYLE_SRC = ["'self'", "'unsafe-inline'"]
# unsafe-inline: 
#   Django Rest Framework inserts the CSRF token via an inline script. DRF will be CSP-compliant in version 3.14 (see https://github.com/encode/django-rest-framework/pull/5740)
#   NuxtJS injects a inline script in index.html
# unsafe-eval:
#   Used by nuxt-vuex-localstorage; PR exists, but maintainer is not very active (see https://github.com/rubystarashe/nuxt-vuex-localstorage/issues/37)
CSP_SCRIPT_SRC = ["'self'", "'unsafe-inline'", "'unsafe-eval'"]



# Monkey-Patch django to use our modified CSRF middleware everywhere
# CSRF middlware class is used as middleware and internally by DjangoRestFramework
from django.middleware import csrf
from reportcreator_api.utils.middleware import CustomCsrfMiddleware
csrf.CsrfViewMiddleware = CustomCsrfMiddleware
CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', default='')
CSRF_TRUSTED_ORIGINS = list(filter(None, CSRF_TRUSTED_ORIGINS.split(';'))) or ['https://*', 'http://*']



# File storage
MEDIA_URL = 'data/'

UPLOADED_IMAGE_STORAGE = 'reportcreator_api.pentests.storages.UploadedImageFileSystemStorage'
UPLOADED_IMAGE_LOCATION = config('UPLOADED_IMAGE_LOCATION', default=MEDIA_ROOT / 'uploadedimages', cast=Path)

UPLOADED_ASSET_STORAGE = 'reportcreator_api.pentests.storages.UploadedAssetFileSystemStorage'
UPLOADED_ASSET_LOCATION = config('UPLOADED_ASSET_LOCATION', default=MEDIA_ROOT / 'uploadedassets', cast=Path)


PDF_RENDER_SCRIPT_PATH = config('PDF_RENDER_SCRIPT_PATH', cast=Path, default=BASE_DIR / '..' / '..' / 'rendering' / 'dist' / 'bundle.js')
PYPPETEER_EXECUTABLE = config('PYPPETEER_EXECUTABLE', default=None)


# MAX_LOCK_TIME should not be less than 2min, because some browsers (Chromium) triggers timers only once per minute if the browser tab is inactive
MAX_LOCK_TIME = timedelta(minutes=2)

SPELLCHECK_URL = config('SPELLCHECK_URL', default=None)


if DEBUG:
    INSTALLED_APPS += [
        'debug_toolbar',
    ]
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]
    INTERNAL_IPS = type(str('c'), (), {'__contains__': lambda *a: True})()
