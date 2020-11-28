import dj_database_url

from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# A list of strings representing the host/domain names that this Django site can serve.
#   - A value beginning with a period can be used as a subdomain wildcard.
#   - '.example.com' will match example.com, www.example.com, and any other subdomain of example.com.
#   -  A value of '*' will match anything.
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '').split(',')

# A list of IP addresses, as strings, that:
#   - Allow the debug() context processor to add some variables to the template context.
#   - Can use the admindocs bookmarklets even if not logged in as a staff user.
#   - Are marked as “internal” (as opposed to “EXTERNAL”) in AdminEmailHandler emails.
INTERNAL_IPS = []


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = { 'default': dj_database_url.config(conn_max_age=600, ssl_require=True) }


# Security
# https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# Redirect all non-HTTPS requests to HTTPS
SECURE_SSL_REDIRECT = True

# Use this header to determine if a request is secure
# (If the app server is behind a proxy that is "swallowing" the HTTPS connection)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Mark the session cookie as 'Secure' (should only be sent over HTTPS by the client)
SESSION_COOKIE_SECURE = True

# Mark the CSRF cookie as 'Secure' (should only be sent over HTTPS by the client)
CSRF_COOKIE_SECURE = True


# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}
