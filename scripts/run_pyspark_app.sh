#!/bin/bash

set -e

# Replace these variables with your actual settings
PROJECT_DIR="./"
CONTAINER_NAME="spark-master"
SPARK_MASTER_URL="spark://spark:7077"
SPARK_ETL_ZIP="src.zip"  # Change the filename here

# Step 1: Create the Python zip archive using the create_apps_pyz.py script
echo "Step 1: Creating the Python zip archive..."
if ! python "${PROJECT_DIR}scripts/zip_apps.py"; then
    echo "Error: Failed to create the Python zip archive."
    exit 1
fi

# Step 3: Run spark-submit inside the container
CONFIG_FILE="$1"
if [ -z "$CONFIG_FILE" ]; then
    echo "Error: Config file path not provided. Usage: $0 /path/to/config.yaml"
    exit 1
fi

APP_NAME=$(basename "$CONFIG_FILE" .yaml)  # Get the app name without the .yaml extension

echo "Step 3: Running spark-submit inside the container with config file: $CONFIG_FILE..."

if ! docker exec -i  "$CONTAINER_NAME" bash -c "spark-submit \
--master $SPARK_MASTER_URL \
--driver-memory 1G \
--executor-memory 1G \
--driver-class-path /opt/jars/clickhouse-jdbc.jar:/opt/jars/postgresql-jdbc.jar: \
--jars /opt/jars/clickhouse-jdbc.jar,/opt/jars/postgresql-jdbc.jar \
--py-files /opt/archive/$SPARK_ETL_ZIP \
--name $APP_NAME \
/opt/src/nightcrawler.py $CONFIG_FILE"; then
    echo "Error: Failed to run spark-submit inside the container."
    exit 1
fi
