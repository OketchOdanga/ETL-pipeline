import psycopg2
import pandas as pd

# Database credentials
db_host = "your_db_host"
db_name = "your_db_name"
db_user = "your_db_user"
db_password = "your_db_password"

# SQL query to extract customer data
query = "SELECT customer_id, first_name, last_name, email, address FROM customers;"

try:
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_password)

    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    # Execute the SQL query
    cur.execute(query)

    # Fetch all the results
    customer_data = cur.fetchall()

    # Get column names from the cursor description
    column_names = [desc[0] for desc in cur.description]

    # Convert the data to a Pandas DataFrame
    df = pd.DataFrame(customer_data, columns=column_names)

    # Print the DataFrame (for demonstration purposes)
    print(df.head())

except psycopg2.Error as e:
    print(f"Error connecting to the database: {e}")

finally:
    # Close the cursor and connection
    if cur:
        cur.close()
    if conn:
        conn.close()

# Save the DataFrame to a CSV file (optional)
df.to_csv("customer_data.csv", index=False)