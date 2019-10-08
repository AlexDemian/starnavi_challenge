FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /starbook
WORKDIR /starbook
RUN apt-get update
COPY /starbook/requirements.txt /starbook
RUN pip3 install -r requirements.txt