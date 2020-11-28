"""
ASGI config for the project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

from dotenv import load_dotenv

from django.core.asgi import get_asgi_application


# Load environment variables from python-dotenv
load_dotenv()

application = get_asgi_application()
