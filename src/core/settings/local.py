from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# A list of strings representing the host/domain names that this Django site can serve.
#   - A value beginning with a period can be used as a subdomain wildcard.
#   - '.example.com' will match example.com, www.example.com, and any other subdomain of example.com.
#   -  A value of '*' will match anything.
ALLOWED_HOSTS = []

# A list of IP addresses, as strings, that:
#   - Allow the debug() context processor to add some variables to the template context.
#   - Can use the admindocs bookmarklets even if not logged in as a staff user.
#   - Are marked as “internal” (as opposed to “EXTERNAL”) in AdminEmailHandler emails.
INTERNAL_IPS = ['127.0.0.1']

# Serve static files with WhiteNoise for the development server
INSTALLED_APPS.insert(0, 'whitenoise.runserver_nostatic')


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
