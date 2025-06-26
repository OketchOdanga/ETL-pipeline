import snowflake.connector
import pandas as pd

# Snowflake credentials
snowflake_account = "your_snowflake_account"
snowflake_user = "your_snowflake_user"
snowflake_password = "your_snowflake_password"
snowflake_database = "your_snowflake_database"
snowflake_schema = "your_snowflake_schema"
snowflake_warehouse = "your_snowflake_warehouse"
snowflake_table = "customers"

try:
    # Establish a connection to Snowflake
    conn = snowflake.connector.connect(
        account=snowflake_account,
        user=snowflake_user,
        password=snowflake_password,
        database=snowflake_database,
        schema=snowflake_schema,
        warehouse=snowflake_warehouse
    )

    # Create a cursor object
    cur = conn.cursor()

    # Load the transformed customer data from the CSV file
    df = pd.read_csv("transformed_customer_data.csv")

    # Iterate over the rows of the DataFrame and insert them into the Snowflake table
    for index, row in df.iterrows():
        sql = f"""
            INSERT INTO {snowflake_table} (customer_id, first_name, last_name, email, address)
            VALUES (%s, %s, %s, %s, %s)
        """
        val = (row['customer_id'], row['first_name'], row['last_name'], row['email'], row['address'])
        cur.execute(sql, val)

    # Commit the changes
    conn.commit()

    print("Data loaded successfully into Snowflake.")

except snowflake.connector.errors.ProgrammingError as e:
    print(f"Error connecting to Snowflake or loading data: {e}")

finally:
    # Close the cursor and connection
    if cur:
        cur.close()
    if conn:
        conn.close()