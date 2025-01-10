"""
Django settings for cnext_backend project.

Generated by 'django-admin startproject' using Django 4.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
import sys

from pathlib import Path
from corsheaders.defaults import default_headers
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv('.env')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
root = lambda *x: os.path.join(BASE_DIR, *x)
sys.path.insert(0, root('apps'))

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-g$rhqtlou5yn8^$)tclvbl5gbb5tf!!jqi(q!&ru5^ldc!os*3'
SECRET_KEY = os.getenv("SECRET_KEY", 'this_is_a_default_secret_key_for_toolshub')
DEBUG = os.getenv("DEBUG", False)
ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = list(default_headers) + ['x-api-key','Set-Cookie','Auth-Code', 'device-type']
CORS_EXPOSE_HEADERS = ['WWW-Authenticate','Set-Cookie']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'corsheaders',
	'django_extensions',
	'rest_framework',
	'rest_framework.authtoken',
	'rest_framework_simplejwt',
]

PROJECT_APPS = [
    "users",
	"rank_predictor",
	"tools",
	"college_compare",
	"college_amenities"
]

if not DEBUG:
	INSTALLED_APPS.append('elasticapm.contrib.django')

INSTALLED_APPS += PROJECT_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
	'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cnext_backend.apps.utils.helpers.custom_authorization.CustomAuthMiddleware',
]

ROOT_URLCONF = 'cnext_backend.urls'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "DIRS": [
            root("templates"),
        ],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = 'cnext_backend.wsgi.application'


DATABASES = {
    'default': {
			'ENGINE': 'django.db.backends.mysql',
			'NAME': os.getenv('MASTER_DB_NAME'),
			'USER': os.getenv('MASTER_DB_USER'),
			'PASSWORD': os.getenv('MASTER_DB_PASSWORD'),
			'HOST': os.getenv('MASTER_DB_HOST'),  # Or an IP Address that your DB is hosted on
			'PORT': os.getenv('MASTER_DB_PORT'),
			 'OPTIONS': {
            'sql_mode': 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_ZERO_DATE,NO_ZERO_IN_DATE,ONLY_FULL_GROUP_BY',
        },
		},
    'slave': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('SLAVE_DB_NAME',''),
            'USER': os.getenv('SLAVE_DB_USER',''),
            'PASSWORD': os.getenv('SLAVE_DB_PASSWORD',''),
            'HOST': os.getenv('SLAVE_DB_HOST','localhost'),  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': '3306',  # Set to empty string for default.
			 'OPTIONS': {
            'sql_mode': 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_ZERO_DATE,NO_ZERO_IN_DATE,ONLY_FULL_GROUP_BY',
			'MAX_CONNECTIONS': 100,
			
        },
        },
}

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

REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'utils.helpers.custom_authorization.CookieHandlerJWTAuthentication',
	),
	'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True
USE_L10N = True
USE_TZ = True


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = root('../static')
MEDIA_ROOT = root('../media')

SIMPLE_JWT = {
	"ACCESS_TOKEN_LIFETIME": timedelta(days=30),
	"REFRESH_TOKEN_LIFETIME": timedelta(days=90),
}

AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend', 'cnext_backend.services.auth_backend_service.EmailAuthBackend')
LOGIN_REDIRECT_URL = '/'

CELERY = {
	'broker_url': 'redis://'+os.getenv('REDIS_HOST','localhost')+':6379/0',
	'result_backend': 'redis://'+os.getenv('REDIS_HOST','localhost')+':6379/0',
	'result_expires': None ,
	'worker_send_task_events': True, # needed for worker monitoring
	'timezone': 'Asia/Kolkata',
	'task_ignore_result': False,
	'task_time_limit':10,
	'task_create_missing_queues':True
}

CELERY_PRIORITY_QUEUE = 'fastlane'
ADMINS = (
			('Subhajeet Dey', 'subhajeet@careers360.com'),
			('Surya Dev Singh', 'surya.dev@careers360.com'),
			('Ayush Jhajriya', 'ayush.jhajriya@careers360.com'),
		)

MANAGERS = ADMINS

CACHES = {
	'default': {
		'BACKEND': 'django_redis.cache.RedisCache',
		'LOCATION': 'redis://'+ os.getenv('REDIS_HOST','localhost') +':6379',
		'OPTIONS': {
			'DB': 2
		},
	},
}

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'formatters': {
		'verbose': {
			'format': '%(levelname)s [%(asctime)s] %(module)s %(message)s'
		},
	},
	'handlers': {
		'console': {
			'level': 'DEBUG',
			'class': 'logging.StreamHandler',
			'formatter': 'verbose'
		},
		'mail_admins': {
			'level': 'ERROR',
			'class': 'django.utils.log.AdminEmailHandler'
		},
		'file': {
	            'level': 'INFO',
	            'class': 'logging.FileHandler',
	            'filename': '/var/log/gunicorn/debug.log',
	        },
		# 'gunicorn': {
		# 	'level': 'DEBUG',
		# 	'class': 'logging.handlers.RotatingFileHandler',
		# 	'formatter': 'verbose',
		# 	'filename': '/var/log/gunicorn/debug.log',
		# 	'maxBytes': 1024 * 1024 * 200,  # 100 mb
		# }
	},
	'loggers': {
		'django': {
			'handlers': ['console','mail_admins','file'],
			'level': 'DEBUG',
			'propagate': True,
		},
		'custom': {
			'handlers': ['console'],
			'level': 'DEBUG',
			'propagate': True,
		},
	},
}

if DEBUG:
	MEDIA_URL = '/media/'
	LOGGING = {}

	INTERNAL_IPS = [
		'127.0.0.1',
	]


WEB_API_KEY = os.getenv("WEB_API_KEY", "")
BASE_URL = os.getenv('API_URL', 'https://toolshub-service.careers360.com/')
FRONTEND_URL = os.getenv('FRONTEND_URL', 'https://www.careers360.com/')
SESSION_DOMAIN_NAME = os.getenv('SESSION_DOMAIN_NAME', '.careers360.com')


USE_S3 = os.getenv('USE_S3', False)
# AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', 'xxxxxx')
# AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', 'xxxxxx')

if USE_S3 == 'True':
	try:
		from .aws import *
	except ImportError:
		pass

CAREERS_BASE_IMAGES_URL = os.getenv('CAREERS_BASE_IMAGES_URL', 'www.careers360.com')


SIMPLE_JWT = {
	"ACCESS_TOKEN_LIFETIME": timedelta(days=30),
	"REFRESH_TOKEN_LIFETIME": timedelta(days=90),
}
JWT_COOKIE_NAME = os.getenv("JWT_COOKIE_NAME", default="refresh_token")
JWT_COOKIE_SAMESITE = os.getenv("JWT_COOKIE_SAMESITE", default="Lax")
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
