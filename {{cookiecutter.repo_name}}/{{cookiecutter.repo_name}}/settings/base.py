import sys
from os.path import abspath, dirname, join


# PATH vars
def here(*args):
    return join(abspath(dirname(__file__)), *args)


def root(*args):
    return join(abspath(PROJECT_ROOT), *args)

PROJECT_ROOT = here("..")

sys.path.insert(0, root('apps'))

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
)

THIRD_PARTY_APPS = (
    'compressor',
    'django_extensions',
)

PROJECT_APPS = ()

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{{cookiecutter.repo_name}}.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{{cookiecutter.repo_name}}.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': root('{{cookiecutter.repo_name}}.db'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = '{{ cookiecutter.timezone }}'

USE_I18N = False

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# Additional locations of static files

STATICFILES_DIRS = (
    root('assets'),
)

# Where collectstatic will collect static files for deployment
STATIC_ROOT = root('collectstatic')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Location for storing user uploaded files
MEDIA_ROOT = root('uploads')

MEDIA_URL = '/uploads/'

TEMPLATE_DIRS = (
    root('templates'),
)

COMPRESS_JS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
]
