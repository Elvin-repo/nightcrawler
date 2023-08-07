import logging

from src.io.clickhouse.clickhouse_io import read_clickhouse_table, write_clickhouse_table
from src.io.csv.csv_io import read_csv, write_csv
from src.io.postgres.postgres import read_postgres_table, write_postgres_table


def read_data(spark, read_config):
    """
    Read data based on the configuration.

    Parameters:
        spark (SparkSession): The initialized SparkSession object.
        read_config (dict): The configuration for reading data.

    Returns:
        DataFrame: The DataFrame containing the data read from the source.
    """
    read_type = read_config["type"]
    if read_type == "csv":
        csv_file_path = read_config["csv_file_path"]
        input_df = read_csv(spark, csv_file_path)
        logging.info("Data has been read from CSV.")
    elif read_type == "clickhouse":
        clickhouse_url = read_config["clickhouse_url"]
        clickhouse_table_name = read_config["clickhouse_table_name"]
        input_df = read_clickhouse_table(spark, clickhouse_url, clickhouse_table_name)
        logging.info("Data has been read from ClickHouse.")
    elif read_type == "postgres":
        logging.info("Data has been successfully read from PostgreSQL.")
        postgres_url = read_config["postgres_url"]
        postgres_table_name = read_config["postgres_table_name"]
        properties = read_config.get("properties", {})
        input_df = read_postgres_table(spark, postgres_url, postgres_table_name, properties)
        logging.info("Data has been successfully read from PostgreSQL.")
    else:
        raise ValueError("Unsupported read type in config.")

    input_df.show()

    return input_df


def write_data(spark, write_configs, input_df):
    """
    Write data based on the configuration.

    Parameters:
        spark (SparkSession): The initialized SparkSession object.
        write_configs (list): The list of configurations for writing data.
        input_df (DataFrame): The DataFrame containing the data to be written.
    """
    for write_config in write_configs:
        write_type = write_config["type"]
        if write_type == "clickhouse":
            clickhouse_url = write_config["clickhouse_url"]
            clickhouse_table_name = write_config["clickhouse_table_name"]
            write_clickhouse_table(input_df, clickhouse_url, clickhouse_table_name)
            logging.info("Data has been successfully written to ClickHouse.")
        elif write_type == "csv":
            csv_file_path = write_config["csv_file_path"]
            write_csv(input_df, csv_file_path)
            logging.info("Data has been successfully written to CSV.")
        elif write_type == "postgres":
            logging.info("Read from PostgreSQL.")
            postgres_url = write_config["postgres_url"]
            postgres_table_name = write_config["postgres_table_name"]
            properties = write_config.get("properties", {})
            write_postgres_table(input_df, postgres_url, postgres_table_name, properties)
            logging.info("Data has been successfully written to PostgreSQL.")
        else:
            raise ValueError("Unsupported write type in config.")
