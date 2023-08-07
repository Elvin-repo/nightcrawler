#!/bin/bash

# Define the versions of the JDBC drivers you want to download
CLICKHOUSE_JDBC_VERSION="0.3.2"
POSTGRESQL_JDBC_VERSION="42.2.6"

# Define the target directory where the jars will be copied
TARGET_DIR="./jars"

# Download the ClickHouse JDBC driver
CLICKHOUSE_JDBC_URL="https://repo1.maven.org/maven2/ru/yandex/clickhouse/clickhouse-jdbc/${CLICKHOUSE_JDBC_VERSION}/clickhouse-jdbc-${CLICKHOUSE_JDBC_VERSION}-shaded.jar"
curl -k -L -o clickhouse-jdbc.jar "$CLICKHOUSE_JDBC_URL"
mv clickhouse-jdbc.jar "$TARGET_DIR"

# Download the PostgreSQL JDBC driver
POSTGRESQL_JDBC_URL="https://jdbc.postgresql.org/download/postgresql-${POSTGRESQL_JDBC_VERSION}.jar"
curl -k -L -o postgresql-jdbc.jar "$POSTGRESQL_JDBC_URL"
mv postgresql-jdbc.jar "$TARGET_DIR"
