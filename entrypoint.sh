#!/bin/sh

python manage.py makemigrations --no-input
python manage.py migrate --no-input

waitress-serve core.wsgi:application
