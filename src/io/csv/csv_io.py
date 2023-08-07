import logging
from pyspark.sql import SparkSession

# Set up logging
logger = logging.getLogger(__name__)


def read_csv(spark, csv_file_path):
    """
    Read data from a CSV file and return a DataFrame.

    Args:
        spark (SparkSession): The Spark session.
        csv_file_path (str): The path to the CSV file.

    Returns:
        DataFrame: The DataFrame containing the data from the CSV file.
    """
    try:
        # Read CSV file into DataFrame with header
        return spark.read.format("csv").option("header", "true").load(csv_file_path)
    except Exception as e:
        logger.error("Error while reading CSV file: %s", e)
        raise


def write_csv(df, csv_file_path):
    """
    Write DataFrame to a CSV file.

    Args:
        df (DataFrame): The DataFrame to write.
        csv_file_path (str): The path to the output CSV file.
    """
    try:
        # Write DataFrame to CSV file with header and overwrite mode
        df.write.format("csv").option("header", "true").mode("overwrite").save(csv_file_path)
        logger.info("Data has been successfully written to CSV: %s", csv_file_path)
    except Exception as e:
        logger.error("Error while writing CSV file: %s", e)
        raise
