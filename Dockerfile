# syntax=docker/dockerfile:1
# https://docs.docker.com/language/python/build-images/
# flask file name must be app.py in this configuration

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .  
# can be written as > COPY . /app 

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]