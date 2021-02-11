import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0%6+ky9)vq2&2pk=xe4f8)2+#sgn3q@74h2!+adq8a3txxe_s+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']

# Application definition
INSTALLED_APPS = [
    'piggybox.apps.PiggyBoxConfig',
    'django.contrib.admin',
    'django.contrib.auth', # コアとなる認証フレームワークとそのデフォルトモデル
    'django.contrib.contenttypes', # Djangoのコンテンツ型システム（モデルにパーミッションを関連付けることができるようにする
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', # リクエストにまたがるセッションを管理する
    'django.contrib.auth.middleware.AuthenticationMiddleware', # セッションを使ってユーザーとリクエストを関連付ける
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',   
]

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

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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
LANGUAGE_CODE = 'ja'

ROOT_URLCONF = 'mysite.urls'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

WSGI_APPLICATION = 'mysite.wsgi.application'


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

IMAGE_ROOT = os.path.join(BASE_DIR, 'images')
IMAGE_URL = '/images/'

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/mypage/'
LOGOUT_REDIRECT_URL='/login/'

# This logs any emails sent to the console.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#３桁区切り
NUMBER_GROUPING = 3