"""
Django settings for PetStore project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _


DEBUG = True

# Base settings
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
SECRET_KEY = '9mzj3@i%b^t2-rjh(%qdhupt=22kcburqyg7agt0(%vozgjxmt'

# Application definition
INSTALLED_APPS = [
    'modeltranslation',
    'storages',
    'moneyed',
    'djmoney',
    'braces',
    'jet',
    'django.contrib.admin',
    #'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tinymce',
    'django_countries',
    'measurement',
    'django_measurement',
    'easy_thumbnails',
    'filer',
    'mptt',
    'taggit',
    'rosetta',
    'backoffice',
    'registration',
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'PetStore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'PetStore.wsgi.application'

# Database
DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':'tapaloeil$PetStore',
        'USER':'tapaloeil',
        'PASSWORD':'Mars!2017',
        'HOST':'tapaloeil.mysql.pythonanywhere-services.com',
    }
}

# Password validation
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
LANGUAGE_CODE = 'fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'cdn/static')
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'cdn/media')
LOCALE_PATHS = (os.path.join(BASE_DIR,"locale"),)


# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'no-reply@paris-pet-store.fr'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'paris.pet.store.test@gmail.com'
EMAIL_HOST_PASSWORD = 'Accenture1'
EMAIL_USE_TLS = True

from .plugin_settings import *

try:
    from .local_settings import *
except ImportError:
    pass
