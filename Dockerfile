FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN pip install -r /app/requirements.txt

COPY src/ .

RUN python manage.py collectstatic --noinput

CMD ["waitress-serve", "core.wsgi:application"]
