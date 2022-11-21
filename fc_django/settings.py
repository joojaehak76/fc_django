"""
Django settings for fc_django project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g$lv)qm$o@zg5fjulaqe4%nuv@-(r+ui%^f*1i#5kp^*!^5do7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

BATON = {
	'SITE_HEADER': '패스트캠퍼스',
	'SITE_TITLE': '패스트캠퍼스 백오피스',
	'INDEX_TITLE': '패스트캠퍼스 관리자페이지',
	'SUPPORT_HREF': 'mailto:admin@admin.com',
	'COPYRIGHT': 'copyright © 2022 Fastcampus',
	'POWERED_BY': '<a href="https://fastcampus.co.kr">Fastcampus</a>',
	'MENU_TITLE': '패스트캠퍼스',
    'MENU': (
        { 'type': 'title', 'label': 'main', 'apps': ('fcuser', 'order', 'product') },
        {
            'type': 'app',
            'name': 'fcuser',
            'label': '사용자',
            'icon': 'fa fa-lock',
            'models': (
                {
                    'name': 'fcuser',
                    'label': '사용자'
                },
            )
        },
        {
            'type': 'free', 'label': '주문', 'default_open': True, 'children': [
                { 'type': 'free', 'label': '주문', 'url': '/admin/order/order/' },
                { 'type': 'free', 'label': '주문 날짜 뷰', 'url': '/admin/order/order/date_view/' },
            ]
        },
        {
            'type': 'app',
            'name': 'product',
            'label': '상품',
            'models': (
                {
                    'name': 'product',
                    'label': '상품'
                },
            )
        },
        { 'type': 'free', 'label': '메뉴얼', 'url': '/admin/manual/' },
    ),
}

INSTALLED_APPS = [
    'baton',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'rest_framework',
    'fcuser.apps.FcuserConfig',
    'order.apps.OrderConfig',
    'product.apps.ProductConfig',
    
    'baton.autodiscover'    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fc_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
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

WSGI_APPLICATION = 'fc_django.wsgi.application'


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

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
