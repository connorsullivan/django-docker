"""
WSGI config for the project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

from dotenv import load_dotenv

from django.core.wsgi import get_wsgi_application


# Load environment variables from python-dotenv
load_dotenv()

application = get_wsgi_application()
