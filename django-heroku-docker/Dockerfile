# pull official base image
FROM python:3.10

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#selenium
RUN apt-get install -y unzip
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
RUN echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get -y update
RUN apt-get -y install google-chrome-stable

RUN curl -OL https://chromedriver.storage.googleapis.com/76.0.3809.126/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip chromedriver
RUN mv chromedriver /usr/bin/chromedriver

# copy project
COPY . .

# collect static files
RUN python manage.py collectstatic --noinput

# run gunicorn
CMD gunicorn hello_django.wsgi:application --bind 0.0.0.0:$PORT