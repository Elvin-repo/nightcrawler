import requests
import logging

clickhouse_url = (
    "http://clickhouse-container:8123"  # Replace "clickhouse" with the container name if using Docker Compose
)


def create_table():
    """
    Creates the 'my_table' in ClickHouse.

    This function sends a CREATE TABLE query to ClickHouse to create the 'my_table'
    if it does not exist already.

    Raises:
        requests.exceptions.RequestException: If the ClickHouse request fails.
    """
    create_table_query = """
    CREATE TABLE IF NOT EXISTS my_table (
        id UInt64,
        name String,
        age UInt8
    ) ENGINE = MergeTree()
    ORDER BY id
    """

    try:
        response = requests.post(clickhouse_url, data=create_table_query)
        response.raise_for_status()
        logging.info("Table 'my_table' created successfully.")
    except requests.exceptions.RequestException as e:
        logging.error("Failed to create table 'my_table': %s", e)


def add_records():
    """
    Adds records to the 'my_table' in ClickHouse.

    This function sends an INSERT INTO query to ClickHouse to add records to the 'my_table'.

    Raises:
        requests.exceptions.RequestException: If the ClickHouse request fails.
    """
    insert_query = """
    INSERT INTO my_table (id, name, age) VALUES
    (1, 'Alice', 30),
    (2, 'Bob', 25),
    (3, 'Charlie', 35)
    """

    try:
        response = requests.post(clickhouse_url, data=insert_query)
        response.raise_for_status()
        logging.info("Records added to 'my_table' successfully.")
    except requests.exceptions.RequestException as e:
        logging.error("Failed to add records to 'my_table': %s", e)


if __name__ == "__main__":
    # Set up logging configuration
    logging.basicConfig(level=logging.INFO)

    # Call the functions to create the table and add records
    create_table()
    add_records()
