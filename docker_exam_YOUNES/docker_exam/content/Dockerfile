FROM debian:latest

RUN apt-get update && apt-get install python3-pip -y && pip install requests

#VOLUME /docker_exam

ADD test_content.py /content/content.py

WORKDIR /content/

CMD python3 content.py
