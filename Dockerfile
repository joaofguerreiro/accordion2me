FROM python:3.6.1
ENV PYTHONBUFFERED 1
MAINTAINER Joao Guerreiro <joaofguerreiro1992@gmail.com>

# Update the default application repository sources list
RUN apt-get update && apt-get -y upgrade
RUN apt-get update --fix-missing

RUN apt-get install -y \
    python-pip \
    python-dev \
    libpq-dev \
    libreadline-dev \
    libssl-dev \
    libjpeg-dev \
    libfreetype6-dev

RUN mkdir /code
ADD . /code/

VOLUME /code
WORKDIR /code

RUN pip install --upgrade pip
RUN pip install -r requirements/docker.pip
