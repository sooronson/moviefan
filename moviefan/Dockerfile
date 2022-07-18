FROM python:3.7


ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITECODE 1

WORKDIR /code

COPY base.txt /code

RUN pip install -r /code/base.txt

COPY . /code