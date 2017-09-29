from settings import *

# --- DEBUG-RELATED SETTINGS ---

PREPEND_WWW = False
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# LOCAL PROJECT URL
PROJECT_URL = "http://0.0.0.0:8000"

# Template debug
TEMPLATES[0]['OPTIONS']['debug'] = True
TEMPLATES[0]['DIRS'] = [
    os.path.join(APPLICATION_ROOT, 'templates'),
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'accordion2me_db',
        'USER': 'root',
        'PASSWORD': 'qwerty',
        'HOST': 'db',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET default_storage_engine=MYISAM, sql_mode=NO_ENGINE_SUBSTITUTION;',
        },
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}
