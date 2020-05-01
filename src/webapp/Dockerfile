FROM ubuntu:20.04
COPY ./hello_world /app/

RUN apt update; apt install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install -y python3 python3-pip
RUN pip3 install -r /app/config/requirements.txt	

EXPOSE 5000

ENTRYPOINT ["python3", "/app/app.py"]

