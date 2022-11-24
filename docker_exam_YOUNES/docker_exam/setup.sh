#!/bin/bash 

echo"Building authentication docker image"
cd authentication
docker build . -f Dockerfile -t authentication_image:latest


echo"Building authorization docker image"
cd ../authorization
docker build . -f Dockerfile -t authoriaztion_image:latest


echo"Building content docker image"
cd ../content
docker build . -f Dockerfile -t content_image:latest


echo "Launching docker-compose"
docker-compose up

echo "Writting the result of the logs in api_test.txt"

echo "Stopping and removing all containers and volumes"
docker-compoe down -v

