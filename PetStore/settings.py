"""
Django settings for PetStore project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9mzj3@i%b^t2-rjh(%qdhupt=22kcburqyg7agt0(%vozgjxmt'

# SECURITY WARNING: don't run with debug turned on in production!

LOGIN_REDIRECT_URL='/'

ACCOUNT_ACTIVATION_DAYS = 7

CURRENCIES = ('USD','EUR','CNY','HKD', 'GBP','JPY')

# Application definition

INSTALLED_APPS = [
    'storages',
    'moneyed',
    'djmoney',
    'braces',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
    'tinymce',
    'django_countries',
    'measurement',
    'django_measurement',
    'taggit',
    'backoffice',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    #'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
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
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'PetStore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


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
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
#STATICFILES_DIRS = [    os.path.join(BASE_DIR, 'static'),]
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'cdn/static')
MEDIA_URL = "/media/"
#MEDIA_ROOT=os.path.join(BASE_DIR, 'media')

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'cdn/media')

#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'testing@example.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_PORT = 1025

# TinyMCE
TINYMCE_JS_URL = STATIC_URL + "tiny_mce/tiny_mce.js"
TINYMCE_JS_ROOT = STATIC_URL + "/tiny_mce"
TINYMCE_SPELLCHECKER=False
TINYMCE_PLUGINS = [
    'safari',
    'table',
    'advlink',
    'advimage',
    'iespell',
    'inlinepopups',
    'media',
    'searchreplace',
    'contextmenu',
    'paste',
    'wordcount'
]

TINYMCE_DEFAULT_CONFIG={
    'theme' : "advanced",
    'plugins' : ",".join(TINYMCE_PLUGINS), # django-cms
    'language' : 'ru',
    "theme_advanced_buttons1" : "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,styleselect,formatselect,fontselect,fontsizeselect,|,spellchecker",
    "theme_advanced_buttons2" : "cut,copy,paste,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,image,cleanup,code,|,forecolor,backcolor,|,insertfile,insertimage",
    "theme_advanced_buttons3" : "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr",
    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_toolbar_align' : "left",
    'theme_advanced_statusbar_location' : "bottom",
    'theme_advanced_resizing' : True,
    'table_default_cellpadding': 2,
    'table_default_cellspacing': 2,
    'cleanup_on_startup' : False,
    'cleanup' : False,
    'paste_auto_cleanup_on_paste' : False,
    'paste_block_drop' : False,
    'paste_remove_spans' : False,
    'paste_strip_class_attributes' : False,
    'paste_retain_style_properties' : "",
    'forced_root_block' : False,
    'force_br_newlines' : False,
    'force_p_newlines' : False,
    'remove_linebreaks' : False,
    'convert_newlines_to_brs' : False,
    'inline_styles' : False,
    'relative_urls' : False,
    'formats' : {
        'alignleft' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-left'},
        'aligncenter' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-center'},
        'alignright' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-right'},
        'alignfull' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-justify'},
        'strikethrough' : {'inline' : 'del'},
        'italic' : {'inline' : 'em'},
        'bold' : {'inline' : 'strong'},
        'underline' : {'inline' : 'u'}
    },
    'pagebreak_separator' : "",
    # Drop lists for link/image/media/template dialogs
    'template_external_list_url': 'lists/template_list.js',
    'external_link_list_url': 'lists/link_list.js',
    'external_image_list_url': 'lists/image_list.js',
    'media_external_list_url': 'lists/media_list.js',
    #
    #'file_browser_callback':'tinyDjangoBrowser'
}

JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

JET_SIDE_MENU_COMPACT = True

import dj_database_url
DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

DEBUG = True

try:
    from .local_settings import *
except ImportError:
    pass
