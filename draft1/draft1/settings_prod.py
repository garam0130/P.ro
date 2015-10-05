from .settings import *  # noqa
import os


if 'X_SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ['X_SECRET_KEY']

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'p_rogramming_db',
        'USER': 'ubuntu',
        'PASSWORD': 'programming_db_password',
        'HOST': '127.0.0.1',
    },
}

