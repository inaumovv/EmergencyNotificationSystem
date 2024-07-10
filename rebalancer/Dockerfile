FROM python:3.10-slim

WORKDIR /usr/src/apps/rebalancer
RUN mkdir -p $WORKDIR/static

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .


RUN celery -A rebalancer worker -E -l info

CMD python manage.py runserver 0.0.0.0:8002