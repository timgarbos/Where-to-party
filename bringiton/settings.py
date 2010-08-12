# Django settings for bringiton project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Tim Garbos', 'timgarbos@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = '/home/bringiton/Where-to-party/bringiton/database'             # Or path to database file if using sqlite3.
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
#MEDIA_ROOT = '/home/garbos/bringiton/bringiton/media/'
MEDIA_ROOT = '/home/bringiton/Where-to-party/bringiton/media/'


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
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'bringiton.urls'

TEMPLATE_CONTEXT_PROCESSORS = (
     "django.core.context_processors.auth", 
    "django.core.context_processors.debug", 
    "django.core.context_processors.i18n", 
    "django.core.context_processors.media", 
    'django.core.context_processors.request',
)

TEMPLATE_DIRS = (
    '/home/garbos/bringiton/bringiton/templates',
    '/Users/kwree/Desktop/Bring.It.On/bringiton/templates',
    '/home/bringiton/Where-to-party/bringiton/templates'
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
    'django.contrib.flatpages',
     'bringiton.menu',
    'tinymce',
    'bringiton.bringiton_base',

)
SITE_ID = 1
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
STATIC_DOC_ROOT = '/home/garbos/bringiton/bringiton/media'

FACEBOOK_API_KEY = '753868bea6d51ce7fe5f681454cc28ed'
FACEBOOK_SECRET_KEY = '09472264b65509762767a8a63af32a8c'
FACEBOOK_INTERNAL = True
FACEBOOK_CACHE_TIMEOUT = 1800


TINYMCE_COMPRESSOR = True
