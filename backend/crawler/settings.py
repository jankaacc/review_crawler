"""
Django settings for crawler project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import dj_database_url
from decouple import Csv, config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY", default="django-insecure-9x9_gy=36l)&rxp1g-rm^o=uv(41n7a73f-*%d!jt$l!dkt*")
HASH_SALT = config("HASH_SALT")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# STATICFILES_DIRS = [os.path.join(BASE_DIR, "crawler", "static_files")]

STATIC_URL = "/assets/static/"
STATIC_ROOT = "/assets/static"

MEDIA_URL = "/assets/media/"
MEDIA_ROOT = "/assets/media"

DOMAIN_NAME = config("DOMAIN_NAME", default="localhost")
ADDITIONAL_ALLOWED_HOSTS = config("ADDITIONAL_ALLOWED_HOSTS", cast=Csv())
ALLOWED_HOSTS = [DOMAIN_NAME] + ADDITIONAL_ALLOWED_HOSTS


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third-party
    "rest_framework",
    "drf_spectacular",
    "django_celery_beat",
    "django_celery_results",
    # local
    "crawler.core",
    "crawler.gp_crawler",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "crawler.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "crawler.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {}
DATABASES["default"] = dj_database_url.parse(
    config("DATABASE_URL"), conn_max_age=600
)


SPECTACULAR_SETTINGS = {
    "TITLE": "CRAWLER API",
    "DESCRIPTION": "",
    "VERSION": "1.0.0",
    "CONTACT": [],
}

REST_FRAMEWORK = {
    "COERCE_DECIMAL_TO_STRING": True,
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


CELERY_BROKER_URL = "redis://cache:6379/0"
CELERY_RESULT_BACKEND = "django-db"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_SERIALIZER = "json"
CELERY_TIMEZONE = TIME_ZONE
