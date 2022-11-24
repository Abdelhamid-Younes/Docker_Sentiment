FROM debian:latest

RUN apt-get update && apt-get install python3-pip -y && pip install requests

#VOLUME /docker_exam

ADD test_authorization.py /authorization/test_authorization.py

WORKDIR /authorization/

CMD python3 test_authorization.py
