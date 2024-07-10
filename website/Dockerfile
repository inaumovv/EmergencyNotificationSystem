FROM python:3.10-slim

WORKDIR /usr/src/apps/website
RUN mkdir -p $WORKDIR/static

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .


RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
RUN echo "yes" | python3 manage.py collectstatic

RUN celery -A website worker -E -l info

CMD python manage.py runserver 0.0.0.0:8000



