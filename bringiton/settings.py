# Django settings for bringiton project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Tim Garbos', 'timgarbos@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'database'             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ee9xi(%n+aah+)-0$=kq15ke*v(v7$59y8^gqm*zu4+&cfzwj='

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'facebook.djangofb.FacebookMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'facebookconnect.middleware.FacebookConnectMiddleware',
)

ROOT_URLCONF = 'bringiton.urls'

TEMPLATE_DIRS = (
    '/home/garbos/bringiton/bringiton/templates',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admindocs',
    'django.contrib.admin',
    #'registration',
    'facebookconnect',
    'bringiton.places',

)
ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.

AUTHENTICATION_BACKENDS = (
    'facebookconnect.models.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

DUMMY_FACEBOOK_INFO = {
    'uid':0,
    'name':'(Private)',
    'first_name':'(Private)',
    'pic_square_with_logo':'http://www.facebook.com/pics/t_silhouette.gif',
    'affiliations':None,
    'status':None,
    'proxied_email':None,
}

FACEBOOK_API_KEY = '7fb85ab9c238d12e2157b0a4e87725c2'
FACEBOOK_SECRET_KEY = 'a5680419635837d925a2175bf95eac8f'
FACEBOOK_INTERNAL = True
FACEBOOK_CACHE_TIMEOUT = 1800
