# Changelog

## TBD
* Prevent migration errors caused by DB queries in license check
* Fix spellcheck returning no results for language=auto
* Do not send unreferenced images to PDF rendering task to reduce memory usage
* Do not export images that are not referenced in exported data
* Fix markdown preview flappy scroll on typing in markdown editor when images are included
* Add an API endpoint to retrieve project data with markdown fields rendered to HTML
* Support validating string fields with RegEx patterns
* Allow accessing designer assets in Chromium during PDF rendering
* Allow requiring a specific CVSS version in CVSS fields
* CVSS 4.0 support


## v2023.136 - 2023-10-30
* Update frontend tech stack to Vue3, Nuxt3, Vuetify3, Typescript
* Update weasyprint to v60
* Increase read timeout in example nginx config
* Prevent duplicate PDF warnings
* Prevent disabling current user
* Allow removing current user from project members
* Prevent footnotes from moving to next page by default in base.css styles
* Default to manual sorting if not finding ordering fields are defined in design
* Fix spellcheck errors when using per-user dictinaries


## v2023.128 - 2023-09-21
* Version history for projects, designs and templates
* UI: Decrease font size of note assignee in list to match finding/section assignee style
* UI: Autofocus note and finding title after create
* UI: More prominent translate template field button
* UI: Include more details on license errors


## v2023.122 - 2023-09-07
* Fix template appears multiple times in search result list when multiple languages match
* Assign notes to users
* Install more Noto Sans fonts to support more languages
* Ignore whitespaces in delete confirm dialogs
* Use proxy config of host in docker-compose containers


## v2023.119 - 2023-08-23
* UI: sticky header and searchbar in list views
* UI: increase file drop area for importing projects, designs and templates
* Configure finding sort order in design
* Allow manual ordering of findings by overriding the default sort order
* Allow ordering of enum choices in design field definition
* Search in all fields for template search
* Add shortcut for creating new findings and notes (Ctrl+J)


## v2023.114 - 2023-08-09
* Remove beta label and change versioning scheme
* Export notes as PDF
* Speed up unit tests for API
* Add CLI command to restore backups
* Sort users alphabetically in selection
* Clear user specific data from Vuex stores on logout
* Filter notifications in API when fetching instead of locally in instances
* Add datalabels plugin for Chart.js in designs
* Fix backward compatible import of templates with old format (format: templates/v1)
* Fix horizontal input field overflows in template editor
* Expose more CVSS information in designs (including CVSS version, base/temporal/environmental score, impact/exploitability subscores)
* Allow adding custom CA certificates to the docker containers during build 


## v0.110 - 2023-07-31
* Multilingual templates
* Support images in templates
* Support creating templates from findings
* UI: Move secondary toolbar actions to a dropdown menu
* UI: Sticky Add button in finding and note list sidebars
* Fix redirect after login for remoteuser default auth provider


## v0.102 - 2023-07-05
* Fix serialization of project check messages


## v0.101 - 2023-07-05
* Implement file upload in user notebook
* Optimize image loading in markdown preview
* Use Argon2 for hashing passwords instead of PBKDF2
* Authentication via API tokens
* Auto-generate OpenAPI schema


## v0.96 - 2023-06-22
* Fix username/password auth not available in login form of community edition


## v0.95 - 2023-06-21
* Store a reference to the original project/design when copying
* Add tags to projects
* UI: Add icons for tags/members/language in project and template list
* Add drag-and-drop PDF designer
* Support SSO via Remote-User HTTP header
* Allow disabling local authentication via username/password to force SSO
* Support configuring default authentication provider via setting DEFAULT_AUTH_PROVIDER
* Fix CSRF error during logout
* Support automatic archiving of finished projects via setting AUTOMATICALLY_ARCHIVE_PROJECTS_AFTER
* Support automatic deletion of old archived projects via setting AUTOMATICALLY_DELETE_ARCHIVED_PROJECTS_AFTER
* Allow importing private designs
* Show warnings and info messages in designer error list
* Log invalid or unsupported CSS rules in PDF designer
* Include font files in repository


## v0.89 - 2023-06-06
* Update dependencies to fix vulnerabilities in python requests (CVE-2023-32681) and webpack (CVE-2023-28154)
* Prevent setting reference-type specific CSS classes to `<ref>` components with slot content
* Prevent buffering full `StreamingHttpResponse` causing high memory load
* Add fonts Roboto Flex, STIX Two Text and Arimo
* Remove non-variable fonts Roboto, Tinos, Lato and Courier Prime
* Configure fallback of common fonts to similar looking fonts (Arial, Helvetica, Times New Roman, Courier New, Verdana)


## v0.87 - 2023-05-24
* Provide (optional) base styles in designer via `@import "/assets/global/base.css";`
* Add `<ref>` component to designs to reference headings, figures, tables and findings
* Support writing markdown inside design HTML templates via `<markdown>` component
* Support markdown attrs for headings
* Allow `<u>` and `<pagebreak />` in markdown
* Provide lodash utility functions in design template
* The update script rebuilds Docker images every seven days to ensure dependencies are updated regularly
* Fix user type field formatting in design rendering
* Add settings for OIDC with Google


## v0.83 - 2023-05-12
* Fix parsing of nested markdown labels (link in footnote in image caption)
* On file not found during PDF rendering: add reference to finding/section in error message
* Add more languages
* Allow confiuring languages via setting PREFERRED_LANGUAGES
* Show current software version in license page
* Allow deleting users via UI
* Fix markdown code block alignment
* Update django to 4.2.1 (security release)


## v0.76 - 2023-05-02
* Release Community Edition
* Add license checks and enforce license limits
* Project archiving and encryption with 4-eye principle
* Improve list editing in markdown editor
* Add a refresh PDF button to the publish project page


## v0.19 - 2023-04-11
* Add private designs visible only to your user
* Support Postgres with PgBouncer in LanguageTool
* Allow storing files in S3 buckets
* Fix backup restore failing for notifications


## v0.18 - 2023-03-13
* Allow setting emojis as custom note icons
* Require re-authentication to enable admin permissions in user sessions
* Test and improve backup and restore logic
* Automatically cleanup unreferenced files and images
* Add words to spellcheck dictionary
* Allow removing and updating roles of imported project members
* Fix label not shown for number fields


## v0.17 - 2023-03-01
* Use variable Open Sans font to fix footnote-call rendering ("font-variant-position: super" not applied)


## v0.16 - 2023-02-23
* Personal and per-project notes
* Use asgi instead of wsgi to support async requests
* Async PDF rendering and spellcheck request
* Support Elastic APM for API and frontend monitoring
* Fetch and display notifications to users
* Add titles to pages in frontend


## v0.15 - 2023-02-06
* Support login via OpenID Connect
* Support offloading PDF rendering to a pool of worker instances
* Spellchecking and highlighting TODOs in string fields
* Make toolbar sticky on top of finding, section and template editor
* Separate scrollbars for side menu and main content
* Rework PDF Viewer


## v0.14 - 2023-01-03
* Data-at-rest encryption for files and sensitive DB data
* Use Session cookies instead of JWT tokens
* Support two factor authentication with FIDO2, TOTP and Backup Codes
* Add user role and permissions for system users
* Support encrypting backups


## v0.13 - 2022-12-16
* Add logo and favicon
* Add per-project user tags
* UI Improvement: create finding dialog: reset template search input after closing dialog, set search query as finding title for new empty findings
* UI Improvement: allow text selection in Markdown editor preview area


## v0.12 - 2022-12-05
* Provide some standard fonts in the docker container
* Customize designs per project
* Allow force changing designs of projects if the old and new design are incompatible
* Update Chromium to fix CVE-2022-4262 (high)


## v0.11 - 2022-11-25
* Compress images to reduce storage size and PDF size
* Manual highlighting of text in markdown code blocks
* Add review status to sections, findings and templates
* UI improvements: rework texts, add icons, more detailed error messages, group warnings by type in the publish page
* Fix rendering of lists of users containing imported project users


## Initial - 2022-11-16
* Begin of changelog
* Collaboratively write pentesting reports
* Render reports to PDF
* Customize report designs to your needs
* Finding Template library
* Export and import designs/templates/projects to share data
* Multi Language support: Engilsh and German
* Spell checking
* Edit locking
* Drag-and-drop image upload
* PDF encryption
* and many more features
