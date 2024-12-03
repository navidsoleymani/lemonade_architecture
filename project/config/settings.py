from datetime import timedelta
from pathlib import Path
import contextlib
import dotenv
import os

from django.utils.translation import gettext_lazy as _
from django.contrib import admin

from pangolin.joker import resolve_bool, resolve_int, get_app_list

dotenv.load_dotenv()

# 0 ----
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('SECRET', 'mY1keY**')
DEBUG = resolve_bool(os.getenv('DEBUG'), False)
ALLOWED_HOSTS = [
    '*',
]
INTERNAL_IPS = [
    '127.0.0.1',
]
INSTALLED_APPS = [
    # 1----
    'corsheaders',
    # 0----
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 2----
    'drf_yasg',
    'rest_framework',
    'django_filters',
    'rest_framework_simplejwt',
    'django_user_agents',
    'useragents',
    # 3----
    'sampleapp.apps.SampleAppConfig',
]
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'config.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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
WSGI_APPLICATION = 'config.wsgi.application'
PG_DATABASE_CONFIG = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.getenv('DB_NAME', 'db'),
    'USER': os.getenv('DB_USER', 'db'),
    'PASSWORD': os.getenv('DB_PASSWORD', 'db'),
    'HOST': os.getenv('DB_HOST', '127.0.0.1'),
    'PORT': os.getenv('DB_PORT', '5432'),
}
SQLITE_DATABASE_CONFIG = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
}
DATABASES = {'default': PG_DATABASE_CONFIG if os.getenv('DB_TYPE', '') == 'postgres' else SQLITE_DATABASE_CONFIG}
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
LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGES = (('en', _('English')), ('fa', _('Farsi')),)
LOCALE_PATHS = [os.path.join(BASE_DIR, 'localepaths/')]
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'staticfilesdirs'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticroot')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediaroot')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# 1 ----
SIMPLE_HISTORY_REVERT_DISABLED = True
APPEND_SLASH = True
AUTH_USER_MODEL = 'hsg_user1.User'
# CORS
CORS_ALLOWED_ORIGINS = ['http://localhost:3000', 'http://127.0.0.1:3000']
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = ('DELETE', 'GET', 'OPTIONS', 'PATCH', 'POST', 'PUT',)
CORS_ALLOW_HEADERS = ('*',)
CORS_ALLOW_CREDENTIALS = True
# Cache settings
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': os.getenv('REDIS_LOCATION', 'redis://127.0.0.1:6379'),
        'TIMEOUT': None,
    }
}
# csrf
CSRF_TRUSTED_ORIGINS = ['http://localhost:8000']

# rest_framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10000/min',
        'user': '1000/min',
    },
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
if not DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = ('rest_framework.renderers.JSONRenderer',)
# Admin Site Config
# admin.AdminSite.get_app_list = get_app_list


# rest_framework_simplejwt
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(
        minutes=int(os.environ.get('SIMPLE_JWT_ACCESS_TOKEN_LIFETIME_MINUTES'))),
    'REFRESH_TOKEN_LIFETIME': timedelta(
        minutes=int(os.environ.get('SIMPLE_JWT_REFRESH_TOKEN_LIFETIME_MINUTES'))),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': True,

    'ALGORITHM': os.environ.get('SIMPLE_JWT_ALGORITHM'),
    'SIGNING_KEY': os.environ.get('SIMPLE_JWT_SIGNING_KEY'),
    'VERIFYING_KEY': '',
    'AUDIENCE': None,
    'ISSUER': None,
    'JSON_ENCODER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': (
        'Bearer',
    ),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': (
        'rest_framework_simplejwt.tokens.AccessToken',
    ),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(
        minutes=int(os.environ.get('SIMPLE_JWT_SLIDING_TOKEN_LIFETIME_MINUTES'))),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(
        minutes=int(os.environ.get('SIMPLE_JWT_SLIDING_TOKEN_REFRESH_LIFETIME_MINUTES'))),

    'TOKEN_OBTAIN_SERIALIZER': 'rest_framework_simplejwt.serializers.TokenObtainPairSerializer',
    'TOKEN_REFRESH_SERIALIZER': 'rest_framework_simplejwt.serializers.TokenRefreshSerializer',
    'TOKEN_VERIFY_SERIALIZER': 'rest_framework_simplejwt.serializers.TokenVerifySerializer',
    'TOKEN_BLACKLIST_SERIALIZER': 'rest_framework_simplejwt.serializers.TokenBlacklistSerializer',
    'SLIDING_TOKEN_OBTAIN_SERIALIZER': 'rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer',
    'SLIDING_TOKEN_REFRESH_SERIALIZER': 'rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer',
}

# Libraries Config
SAMPLE_APP = {
    'SERIALIZER_BASE_CLASSES': {
        'BASE': 'hsg_user1.utils.serializers.BaseModelSerializerClass',
        'CREATE': 'hsg_user1.utils.serializers.BaseCreateModelSerializerClass',
        'LIST': 'hsg_user1.utils.serializers.BaseListModelSerializerClass',
        'RETRIEVE': 'hsg_user1.utils.serializers.BaseRetrieveModelSerializerClass',
        'UPDATE': 'hsg_user1.utils.serializers.BaseUpdateModelSerializerClass',
        'DESTROY': 'hsg_user1.utils.serializers.BaseDestroyModelSerializerClass',
    }
}
