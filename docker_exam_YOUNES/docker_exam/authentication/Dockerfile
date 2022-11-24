FROM debian:latest

RUN apt-get update && apt-get install python3-pip -y && pip install requests

ENV LOG 1

#VOLUME /docker_exam

ADD test_authentication.py /authentication/test_authentication.py

WORKDIR /authentication/

CMD python3 test_authentication.py
# ./my_vol/api_test.txt
