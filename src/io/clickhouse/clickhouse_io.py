import logging
from src.common.utils import not_implemented_func


def read_clickhouse_table(spark, clickhouse_url, table_name):
    """
    Read data from a ClickHouse table using Spark DataFrame.

    Args:
        spark (SparkSession): The initialized SparkSession object.
        clickhouse_url (str): The JDBC URL for the ClickHouse connection.
        table_name (str): The name of the ClickHouse table to read from.

    Returns:
        DataFrame: The DataFrame containing the data from the ClickHouse table.
    """
    logger = logging.getLogger(__name__)
    try:
        logger.info("Reading data from ClickHouse table: %s", table_name)
        df = spark.read.format("jdbc").option("url", clickhouse_url).option("dbtable", table_name).load()
        logger.info("Data read successfully from ClickHouse table: %s", table_name)
        return df
    except Exception as e:
        logger.error("Error while reading data from ClickHouse table: %s. Error: %s", table_name, e)
        raise


def write_clickhouse_table(df, clickhouse_url, table_name):
    """
    Write data from a DataFrame to a ClickHouse table.

    Parameters:
        df (pyspark.sql.DataFrame): The DataFrame containing the data to be written to the table.
        clickhouse_url (str): The URL of the ClickHouse server.
        table_name (str): The name of the ClickHouse table where the data will be written.

    Raises:
        Exception: If an error occurs while writing data to the ClickHouse table.
    """
    # Custom message to be passed to not_implemented_func
    message = "Function 'write_clickhouse_table' is not implemented yet."

    # Call the not_implemented_func and pass the custom message as a parameter
    not_implemented_func(message)

    # Add your actual implementation code here
    # For now, just passing to make it a valid function
    pass
