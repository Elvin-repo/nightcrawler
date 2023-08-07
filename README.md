# Spark Standalone Cluster with Docker and Docker Compose

This repository provides a setup for running a Spark standalone cluster using Docker and Docker Compose. It enables you to develop and deploy PySpark applications in a containerized environment. Follow the steps below to get started.

## Prerequisites

## Setup Instructions

https://medium.com/@elvinrego/building-a-scalable-config-driven-etl-framework-in-apache-spark-db98be41116b

## Spark Connections

1. [Clickhouse](https://clickhouse.tech/): An open-source columnar database management system for online analytical processing (OLAP).
2. [Druid](https://druid.apache.org/): An open-source distributed data store designed for real-time analytics on large datasets.
3. [Kafka](https://kafka.apache.org/): An open-source distributed event streaming platform for building real-time data pipelines and streaming applications.
4. [PostgreSQL](https://www.postgresql.org/): An open-source relational database management system.

You can explore these links to learn more about how Spark can connect and interact with these data sources.


To ensure code quality and formatting, you can use the following commands:

## Other

1. Check your Spark application code for style and PEP8 compliance:
    ```bash
   flake8
2. Automatically format your code according to Black's rules:
    ```bash
   black .
