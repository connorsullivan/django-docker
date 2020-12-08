FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r /app/requirements.txt

COPY django/ .

RUN python manage.py collectstatic --no-input

COPY entrypoint.sh .

ENTRYPOINT ["sh", "entrypoint.sh"]
