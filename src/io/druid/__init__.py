def write_druid_table(druid_url, pandas_df, datasource, dimensions, index):
    """
    Write data to a Druid datasource using the Avatica JDBC driver.

    Args:
        druid_url (str): The Druid broker URL for the connection.
        pandas_df (DataFrame): The DataFrame containing the data to be written.
        datasource (str): The name of the Druid datasource to write to.
        dimensions (list): A list of dimension column names.
        index (str): The column name to be used as the Druid timestamp.

    Returns:
        None
    """
    druid_conn = connect(host=druid_url)
    druid_conn.load(datasource, pandas_df, dimensions=dimensions, index=index)
