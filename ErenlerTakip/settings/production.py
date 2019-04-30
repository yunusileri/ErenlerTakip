#   Sunucu Ayarları

from ErenlerTakip.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['192.168.182.129']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'erenler',
        'USER': 'yunus',
        'PASSWORD': '1',
        'HOST': 'localhost',
        'PORT': '',
    }
}
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
