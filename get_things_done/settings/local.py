from .base import *  # noqa

DEBUG = True
ALLOWED_HOSTS = [
    "127.0.0.1",
]
INTERNAL_IPS = ["127.0.0.1"]

# EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# Set DJANGO_DISABLE_LOCAL_CACHE in environment variables
# to disable cache during development
CACHE_BACKEND = "django.core.cache.backends.locmem.LocMemCache"
CACHES = {
    "default": {
        "BACKEND": CACHE_BACKEND,
    },
}
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

# TOOLBAR CONFIGURATION
# https://github.com/django-debug-toolbar/django-debug-toolbar#installation

INSTALLED_APPS += [  # noqa
    "debug_toolbar",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
] + MIDDLEWARE  # noqa
