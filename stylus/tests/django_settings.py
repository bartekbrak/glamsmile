from django.conf.global_settings import *
import os


STATIC_ROOT = MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')
STATIC_URL = MEDIA_URL = "/media/"
INSTALLED_APPS = (
    "stylus",
)
STYLUS_MTIME_DELAY = 2
STYLUS_OUTPUT_DIR = "STYLUS_CACHE"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'stylus': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}
