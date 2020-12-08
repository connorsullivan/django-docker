from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


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
