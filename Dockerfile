FROM python:3.6-slim

LABEL maintainer="sebastian_cheung@live.com"

USER root

COPY . /app

WORKDIR /app


RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

ENV FLASK_APP application

CMD ["python", "application.py"]

