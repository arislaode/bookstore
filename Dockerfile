FROM python:3.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /bookstore_project

COPY Pipfile Pipfile.lock /bookstore_project/
RUN pip install pipenv && pipenv install --system

COPY . /bookstore_project/