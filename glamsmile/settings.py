import os
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
TIME_ZONE = 'Europe/Warsaw'
LANGUAGE_CODE = 'pl'
SITE_ID = 1
USE_I18N = False
USE_L10N = False

MEDIA_ROOT = ''
MEDIA_URL = ''

STATIC_ROOT = os.path.abspath(os.path.join(PROJECT_PATH, 'static'))
STATIC_URL = '/static/'

STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '6wx=x85yz45u_ujg9^j@t7#)2_lgahy)!*w&amp;$cl@e^6d_%^7yk'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #django-cms
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    #'cms.middleware.toolbar.ToolbarMiddleware',  # add for front end editing
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

ROOT_URLCONF = 'glamsmile.urls'

WSGI_APPLICATION = 'glamsmile.wsgi.application'

TEMPLATE_DIRS = (
    '/'.join((PROJECT_PATH, 'templates')),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    #django-cms
    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',
    # django-cms plugins
    # 'cms.plugins.file',
    'cms.plugins.link',
    'cms.plugins.picture',
    # 'cms.plugins.teaser',
    'cms.plugins.text',
    # 'cms.plugins.video',
    # 'cms.plugins.googlemap',
    # 'cms.plugins.flash',
    # misc
    'debug_toolbar',
    'stylus',
    # main
    'glamsmile',
    'mylink_cmsplugin'
)


from settings_local import *
from cms_settings import *
