import os

from pathlib import Path
import os


<<<<<<< HEAD

import os
import dj_database_url


=======
>>>>>>> cd7aa9c6 (App)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')

STATIC_DIR=os.path.join(BASE_DIR,'static')

<<<<<<< HEAD
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

=======
>>>>>>> cd7aa9c6 (App)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dhup^y*ngb9w+-8h2=w^s+ucy0-p7_8f_3c!7tn!jy2xlmyh8_'

# SECURITY WARNING: don't run with debug turned on in production!
<<<<<<< HEAD
# ...

DEBUG = False

ALLOWED_HOSTS = [
    'smartdoc.herokuapp.com',
    
]

# ...
=======
DEBUG = True

ALLOWED_HOSTS = []
>>>>>>> cd7aa9c6 (App)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
<<<<<<< HEAD
     # ...
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ...
=======
>>>>>>> cd7aa9c6 (App)
]

ROOT_URLCONF = 'healthcare.urls'

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

WSGI_APPLICATION = 'healthcare.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

<<<<<<< HEAD
# Parse database configuration from DATABASE_URL environment variable
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}



#DATABASES = {
    #'default': {
     #   'default': dj_database_url.config(default='postgres://localhost'),
      #  'ENGINE': 'django.db.backends.mysql',
       # 'NAME': 'healthcare_db',
        #'USER':'root',
        #'PASSWORD':'5351',
        #'HOST':'127.0.0.1',
        #'PORT':'3306'
    #}
#} 






=======
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'healthcare_db',
        'USER':'root',
        'PASSWORD':'5351',
        'HOST':'127.0.0.1',
        'PORT':'3306'
    }
}


>>>>>>> cd7aa9c6 (App)
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'




STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'core.user'

LOGIN_URL = 'login'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

