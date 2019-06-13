import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCAL_INSTANCE = lambda *args: os.path.join(os.path.dirname(__file__), *args)
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "r(pr_guckt07xaelii=fkn^qpr3=l=7%bh0_37uebmzndbemqw"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get("DEBUG", 0))
DEBUG = False if DEBUG == 0 else True
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
DEBUG_TOOLBAR_PATCH_SETTINGS = False
TEMPLATE_DEBUG = DEBUG
COMPRESS_CSS_FILTERS = [
    "compressor.filters.css_default.CssAbsoluteFilter",
    "compressor.filters.cssmin.CSSMinFilter",
]
COMPRESS_JS_FILTERS = ["compressor.filters.jsmin.JSMinFilter"]


ALLOWED_HOSTS = ["*", "rdenadai.com.br", "rdenadai-resume.herokuapp.com"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "storages",
    "compressor",
    "pagedown",
    "info",
    "blog",
]

MIDDLEWARE = [
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.gzip.GZipMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
]

ROOT_URLCONF = "resume.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(PROJECT_PATH, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.csrf",
                "django.template.context_processors.request",
                "django.template.context_processors.static",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    #  'django.contrib.staticfiles.finders.DefaultStorageFinder',
    "compressor.finders.CompressorFinder",
)

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, "../media"),
)


WSGI_APPLICATION = "resume.wsgi.application"

if DEBUG:
    # Database
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(PROJECT_PATH, "db.sqlite3"),
        }
    }
else:
    # Database
    import dj_database_url

    DATABASES = {"default": dj_database_url.config(default="postgres://localhost")}
    CACHES = {
        "default": {
            "BACKEND": "django_bmemcached.memcached.BMemcached",
            "LOCATION": os.environ.get("MEMCACHEDCLOUD_SERVERS").split(","),
            "TIMEOUT": 500,
            "OPTIONS": {
                "username": os.environ.get("MEMCACHEDCLOUD_USERNAME"),
                "password": os.environ.get("MEMCACHEDCLOUD_PASSWORD"),
                "no_block": True,
                "tcp_nodelay": True,
                "tcp_keepalive": True,
                "remove_failed": 4,
                "retry_timeout": 2,
                "dead_timeout": 10,
                "_poll_timeout": 2000,
            },
        },
        "compressor": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
            "LOCATION": "compressor",
        },
    }
    COMPRESS_CACHE_BACKEND = "compressor"


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
SITE_ID = 2

# Static files (CSS, JavaScript, Images)
MEDIA_ROOT = os.path.join(PROJECT_PATH, "../media/")
STATIC_ROOT = os.path.join(PROJECT_PATH, "../static/")
COMPRESS_ROOT = STATIC_ROOT
MEDIA_URL = "/media/"
STATIC_URL = "/static/"
UPLOAD_ROOT = MEDIA_ROOT
MARKDOWN_EXTENSIONS = [
    "markdown.extensions.extra",
    "markdown.extensions.codehilite",
    "markdown.extensions.nl2br",
    "markdown.extensions.wikilinks",
]
LOCALE_PATHS = (os.path.join(PROJECT_PATH, "locale"),)
# WhiteNoise settings
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# AWS CONNECTION
USE_S3 = not DEBUG
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_QUERYSTRING_AUTH = False
S3_URL = "https://%s.s3.amazonaws.com/" % AWS_STORAGE_BUCKET_NAME

if USE_S3:
    DEFAULT_FILE_STORAGE = "home.s3utils.MediaS3BotoStorage"
    THUMBNAIL_DEFAULT_STORAGE = "home.s3utils.MediaS3BotoStorage"
    MEDIA_URL = S3_URL + "media/"
    AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
        "Expires": "Thu, 31 Dec 2099 20:00:00 GMT",
        "Cache-Control": "max-age=94608000",
    }
