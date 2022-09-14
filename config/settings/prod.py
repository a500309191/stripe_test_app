from .base import *
from decouple import config, Csv
import django_on_heroku

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
SECRET_KEY = config("SECRET_KEY")
DEBUG = False

DEBUG_PROPAGATE_EXCEPTIONS = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'main_format': {
            'format': '{asctime} - {levelname} - {module} - {filename} - {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'main_format',
        },
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'main_format',
            'filename': 'information.log',
        },
    },
    'loggers': {
        'main': {
            'handler': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}

# heroku_Settings
django_on_heroku.settings(locals(), staticfiles=False)
del DATABASES['default']['OPTIONS']['sslmode']


