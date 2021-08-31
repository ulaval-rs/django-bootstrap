from .base import *  # noqa: F403
import os

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
    },
}

# Email
SERVER_EMAIL = "su@email.com"
DEFAULT_FROM_EMAIL = "webmaster@localhost"
EMAIL_SUBJECT_PREFIX = "[Django] "
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "localhost"
EMAIL_PORT = 25

# Storage, static and media
DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
STATIC_URL = "/static/"
STATIC_ROOT = "/usr/src/static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = "usr/src/media/"
