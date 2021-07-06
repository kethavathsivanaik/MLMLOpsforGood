FROM python:3.8
LABEL maintainer="Visual Velocity"

COPY . /train
WORKDIR /train
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install net-tools -y
RUN chmod +x entrypoint.sh

ENTRYPOINT /train/entrypoint.sh ; /bin/bash ; 


