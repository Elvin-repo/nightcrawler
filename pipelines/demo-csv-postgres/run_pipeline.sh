#!/bin/bash

set -e

# Replace these variables with your actual settings
PROJECT_DIR="./"
PYSPARK_SCRIPT="scripts/run_pyspark_app.sh"  # The path to the run_pyspark_app.sh script
CONFIG_FILE="/opt/pipelines/demo-csv-postgres/csv_to_postgres.yaml"  # The path to the clickhouse_csv.yaml file

# Step 2: Run the PySpark script
echo "Step 2: Running the PySpark script with config file: $CONFIG_FILE..."
if ! bash "${PROJECT_DIR}${PYSPARK_SCRIPT}" "$CONFIG_FILE"; then
    echo "Error: Failed to run the PySpark script."
    exit 1
fi
