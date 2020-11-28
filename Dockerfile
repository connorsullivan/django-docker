FROM python:3-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY src/ .

RUN python manage.py collectstatic --noinput

CMD ["waitress-serve", "core.wsgi:application"]
