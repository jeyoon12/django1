"""
Django settings for django1 project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from django.urls.base import reverse_lazy
from django.conf.global_settings import LOGIN_REDIRECT_URL,\
    AUTHENTICATION_BACKENDS

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# login_required 데코레이터가 띄우는 로그인 URL을 설정
LOGIN_URL = reverse_lazy('cl:signin') # LOGIN_URL 작성 시 자동 완성 사용하면 안됨

# 소셜 로그인 완료 후 이동할 URL 주소를 저장하는 변수 -> django 기능
LOGIN_REDIRECT_URL = reverse_lazy('blog:index')

# social_django 어플리케이션의 설정값

# 인증 관련 모듈 추가
AUTHENTICATION_BACKENDS = (
    # 구글 로그인 처리 관련 파이썬 클래스 추가
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GooglePlusAuth',
    # 소셜로그인 정보를 django의 User 모델 클래스에 저장하기 위한 클래스
    'django.contrib.auth.backends.ModelBackend'
    # 그 다음 아래 templates 변수로 이동 
    )

# 구글 개발자 사이트에서 발급 받은 ID, PASSWORD 복붙해 저장
SOCIAL_AUTH_GOOGLE_PLUS_KEY = '610044575633-g28mq2kgb7mj72a9bgg91phussgqjf4c.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_PLUS_SECRET = 'aw91TfxCxogkb4_K4eiaA-oI'
# django1 하위 urls.py의 urlpatterns로 이동해 base.html 연장하고 구글로 로그인하기 추가하기

'''
위 LOGIN_URL은 질문 추가 버튼을 눌렀을 때 ~/account~ 페이지로 넘어가는 것이 아니라 로그인하는 페이지로 넘어가게 함
 
1. reverse_lazy와 reverse 공통점: 등록된 URL의 별칭을 바탕으로 URL을 반환하는 함수
2. 차이점: URL을 반환하는 시기
- reverse: 함수 호출 되자마자 등록된 URL에서 찾음
- reverse_lazy: 웹서버가 정상적으로 실행된 뒤에 등록된 URL에서 찾음
- 헛갈리는 경우 모든 파이썬코드에서 reverse_lazy를 써도 무방함
'''


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4nwhudc)rl2!&pte$ksge$17ms=%2sve6l!pr2)#zv*nkb%x9$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
# 프로젝트 내에서 실행할 어플리케이션을 등록/관리하는 변수
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth', # 인증에 관한 어플리케이션 -> 사용자 관리
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookmark', # 웹 프로젝트에 bookmark 어플리케이션이 존재함을 등록
    'vote', 
    'customlogin',
    'blog',
    # pip install social-auth-app-django 명령어로 모듈이 설치돼있어야 사용 가능
    'social_django',
    # 후 위의 24번째 줄 소셜 로그인 변수로 이동)
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

ROOT_URLCONF = 'django1.urls'

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
                # 소셜로그인 처리를 위한 템플릿 관련 함수 추가
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                # authentification_backends 변수 아래로 이동
            ],
        },
    },
]

WSGI_APPLICATION = 'django1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# 클라이언트의 요청으로 저장하는 미디어파일(이미지, 첨부파일) 설정
# MEDIA_URL: URL 주소로 파일 주소를 접근할 때 사용하는 URL을 저장하는 변수

# 127.0.0.1:8000/files/로 시작하는 경로는 미디어 파일을 불러오는 것으로 판단함
MEDIA_URL = '/files/'

# MEDIA_ROOT: 실제 파일이 저장되는 하드웨어 경로
# BASE_DIR: 웹프로젝트가 저장된 경로
# os.path.join(기존경로, 새 경로): 기존 경로에 새경로를 붙인 문자열을 생성

# 현재 프로젝트 폴더/files에 클라이언트가 업로드한 파일이 저장되도록 설정
MEDIA_ROOT = os.path.join(BASE_DIR, 'files')
# C:/files/폴더에 미디어파일이 저장되도록 설정하려면: MEDIA_ROOT = 'c:/files'

# MEDIA_URL과 MEDIA_ROOT를 설정한 뒤, 메인 URLConf에서 URL과 하드웨어 경로를 매칭하는 작업

# django1의 urls.py 60번째 줄 settings, static import로 이동




