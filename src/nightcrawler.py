import sys
import os
import logging
import yaml
from pyspark.sql import SparkSession
from src.cerebro import read_data, write_data
from src.common.utils import setup_logging


def create_spark_session():
    """
    Create a Spark session if it does not exist, or get an existing Spark session.

    Returns:
        SparkSession: The initialized or existing SparkSession object.
    """
    spark = SparkSession.builder.getOrCreate()
    return spark


def process_data(spark, config):
    """
    Process data based on the configuration.

    Parameters:
        spark (SparkSession): The initialized SparkSession object.
        config (dict): The main configuration for the data processing.
    """
    try:
        read_config = config["read"]
        input_df = read_data(spark, read_config)
        write_configs = config["writes"]
        write_data(spark, write_configs, input_df)
    except Exception as e:
        # Log the error and any relevant information
        logging.error(f"An error occurred while reading the yaml file: {e}")
        # Raise the error again to propagate it to the caller
        raise


def get_config_file_path():
    """
    Get the configuration file path from the command-line arguments.

    Returns:
        str: The path to the configuration file.
    """
    if len(sys.argv) < 2:
        raise ValueError("Config file path not provided. Usage: python /pipelines/clickhouse_csv.yaml")
    config_file = sys.argv[1]
    if not os.path.isfile(config_file):
        raise FileNotFoundError(f"Config file not found: {config_file}")
    return config_file


def main():
    config_file = get_config_file_path()
    log_name = os.path.splitext(config_file)[0] + ".log"

    # Set up logging with the application name
    setup_logging(log_name)
    logger = logging.getLogger(__name__)
    logger.info("Starting ETL pipeline.")

    # Create the SparkSession
    spark = create_spark_session()
    logger.info("SparkSession created.")

    try:
        # Load the configuration from the YAML file
        with open(config_file, "r") as yaml_file:
            config = yaml.safe_load(yaml_file)
        logger.info("Configuration loaded from %s.", config_file)

        # Process the data using the loaded configuration
        process_data(spark, config)
        logger.info("Data processing completed.")
    except Exception as e:
        # Log any errors that occurred during the process
        logger.error("An error occurred: %s", e)
    finally:
        # Stop the SparkSession and log the completion of the ETL pipeline
        spark.stop()
        logger.info("ETL pipeline ended.")


if __name__ == "__main__":
    main()
