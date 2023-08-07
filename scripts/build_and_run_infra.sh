#!/bin/bash

# Build the Apache Spark container using the Dockerfile_spark in the current directory
# docker-compose down --volumes
docker build -t spark-image   -f ./Dockerfile_spark .
docker build -t python-image -f ./Dockerfile_python .
docker-compose up -d
