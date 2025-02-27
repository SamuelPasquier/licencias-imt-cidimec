"""
Django settings for page_permisos project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os 
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ
# ALLOWED_HOSTS = ['www.imt.ucb.edu.bo', '127.0.0.1']
# Usar solo en caso de pruebas
ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:    
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registro',
    'consultas',
    'gestion',
    'login',
    'logout',
    'consulta_permisos_docentes',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'page_permisos.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "registro" / "templates",
            BASE_DIR / "consultas" / "templates",
            BASE_DIR / "gestion" / "templates",
            BASE_DIR / "consulta_permisos_docentes" / "templates",
        ],
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

WSGI_APPLICATION = 'page_permisos.wsgi.application'


LOGIN_REDIRECT_URL = '/cidimec/licencias-imt/gestion/'
LOGOUT_REDIRECT_URL = '/cidimec/licencias-imt/login/'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'imtucbco_licencias',
#         'USER': 'imtucbco_licencias',
#         'PASSWORD': 'C1D1M3C.imt',
#         'HOST': '127.0.0.1',  # O la dirección de tu servidor MySQL
#         'PORT': '3306',           # Por lo general, el puerto de MySQL es 3306
#     }
# }

DATABASES = {
    'default': dj_database_url.config(
        default= 'postgresql://postgres:postgres@localhost/postgres',
        conn_max_age=600
    )
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'cidimec/licencias-imt/static_files/'
STATICFILES_DIRS = [
    BASE_DIR / 'registro/static',
]
STATIC_ROOT = BASE_DIR / 'static_files'

if not DEBUG:    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')
    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Configuración para envío de emails
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = "az1-ts2.a2hosting.com"
#EMAIL_USE_TLS = True
#EMAIL_PORT = 465
#EMAIL_HOST_USER = 'info@imt.ucb.edu.bo'
#EMAIL_HOST_PASSWORD = 'C1D1M3C.imt'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "licencias-imt.imt-ucb.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 465
EMAIL_HOST_USER = 'info@licencias-imt.imt-ucb.com'
EMAIL_HOST_PASSWORD = 'C1D1M3C.imt'


#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = "smtp.gmail.com"
#EMAIL_USE_TLS = True
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'info.cidimec@gmail.com'
#EMAIL_HOST_PASSWORD = 'wtlg vofh lecj vsmh'

# Media files
MEDIA_URL = '/cidimec/licencias-imt/media/'
MEDIA_ROOT = BASE_DIR / 'media'


CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
