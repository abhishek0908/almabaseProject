"""
Django settings for almabase project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR/'static'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_o2_8x$6t5@q3^%#0q&mx4!@p^a0=3^)4k%v@%pzup&-#9%cu2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
SITE_ID =2
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'prevyear',
    'django.contrib.sites',
    
# google auth related setting 
    'allauth',
     'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

# google auth related setting 
SOCIALACCOUNT_PROVIDER={
"google" : {
    "SCOPE":[
        "profile",
        "email"
    ], 
    "AUTH_PARAMS" :{"access_type":"online"}
}
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'almabase.urls'

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

WSGI_APPLICATION = 'almabase.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR]
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'

# Path where media is stored'
MEDIA_ROOT = BASE_DIR / 'media'

MESSAGE_TAGS = { messages.ERROR: 'danger', }



# Email Configuration
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# DEFAULT_FROM_EMAIL = "abhishekudiya8@gmail.com"  # Replace with your desired default sender email address
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = "abhishekudiya09@gmail.com"  # Replace with your SendGrid username
EMAIL_HOST_PASSWORD = "denfzyetnfoemecx"  # Replace with your SendGrid password
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# google auth related setting 
AUTHENTICATION_BACKENDS = {
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend"
}
LOGIN_DIRECT_URL = "profile/"
LOGIN_REDIRECT_URL = "profile/"

# google auth related setting 
# Request email from Google
SOCIALACCOUNT_QUERY_EMAIL = True

# Require users to have an email address associated with their account
ACCOUNT_EMAIL_REQUIRED = True

# Enforce unique email addresses for user accounts
ACCOUNT_UNIQUE_EMAIL = True

SOCIALACCOUNT_LOGIN_ON_GET=True


# Setting for connect allauth.py to redirect page if email exists
SOCIALACCOUNT_ADAPTER = 'app.allauth.CustomSocialAccountAdapter'
