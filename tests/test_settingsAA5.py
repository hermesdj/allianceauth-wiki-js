"""
Alliance Auth v5 Test Suite Django settings.
"""

from allianceauth.project_template.project_name.settings.base import *  # noqa

SITE_URL = "https://example.com"
CSRF_TRUSTED_ORIGINS = [SITE_URL]

# Celery configuration
CELERY_ALWAYS_EAGER = True  # Forces celery to run locally for testing
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

INSTALLED_APPS += [  # noqa
    'wikijs',
]

ROOT_URLCONF = 'tests.urls'

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

LOGGING = None

# Register an application at https://developers.eveonline.com for Authentication
# & API Access and fill out these settings. Be sure to set the callback URL
# to https://example.com/sso/callback substituting your domain for example.com
# Logging in to auth requires the publicData scope (can be overridden through the
# LOGIN_TOKEN_SCOPES setting). Other apps may require more (see their docs).
ESI_SSO_CLIENT_ID = '123'
ESI_SSO_CLIENT_SECRET = '123'
ESI_SSO_CALLBACK_URL = '123'
ESI_USER_CONTACT_EMAIL = 'ci@example.com'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://localhost:6379/1",
    }
}

WIKIJS_API_KEY = "abc-123"
WIKIJS_URL = "http://localhost/"

# Suppress Django 5 security warnings in tests
STATICFILES_DIRS = []
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
