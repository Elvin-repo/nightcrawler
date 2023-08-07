import logging
from pyspark.sql import SparkSession

# Create a logger for this module
logger = logging.getLogger(__name__)


def read_postgres_table(spark, postgres_url, table_name, connection_properties):
    """
    Read data from a PostgreSQL table using Spark DataFrame.

    Parameters:
        spark (SparkSession): The initialized SparkSession object.
        postgres_url (str): The JDBC URL for the PostgreSQL connection.
        table_name (str): The name of the PostgreSQL table to read from.
        connection_properties (dict): Dictionary containing connection properties for the JDBC connection,
                                      including 'user' and 'password'.

    Returns:
        DataFrame: The DataFrame containing the data from the PostgreSQL table.
    """
    try:
        # Load data from the PostgreSQL table into a DataFrame
        df = spark.read.jdbc(url=postgres_url, table=table_name, properties=connection_properties)

        # Cache the DataFrame in memory for faster access if needed
        # df.cache()

        logger.info("Successfully read data from PostgreSQL table: %s", table_name)
        return df
    except Exception as e:
        logger.error("An error occurred while reading data from the PostgreSQL table: %s", e)
        raise


def write_postgres_table(df, postgres_url, table_name, connection_properties):
    """
    Write data from a Spark DataFrame to a PostgreSQL table.

    Parameters:
        df (pyspark.sql.DataFrame): The DataFrame containing the data to be written to the table.
        postgres_url (str): The JDBC URL for the PostgreSQL connection.
        table_name (str): The name of the PostgreSQL table where the data will be written.
        connection_properties (dict): Dictionary containing connection properties for the JDBC connection,
                                      including 'user' and 'password'.

    Raises:
        Exception: If an error occurs while writing data to the PostgreSQL table.
    """
    try:
        # Write data from DataFrame to the PostgreSQL table using bulk insert mode
        df.write.jdbc(url=postgres_url, table=table_name, mode="overwrite", properties=connection_properties)

        logger.info("Data has been successfully written to PostgreSQL table: %s", table_name)
    except Exception as e:
        logger.error("An error occurred while writing data to the PostgreSQL table: %s", e)
        raise
