# pip install psycopg2-binary
import psycopg2
from datetime import datetime

# Database connection parameters
db_params = {
    'dbname': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',  # Change this if your database is hosted elsewhere
    'port': '5432'  # Default PostgreSQL port
}

# Create a connection to the PostgreSQL database
conn = psycopg2.connect(**db_params)

# Create a cursor object to interact with the database
cur = conn.cursor()

# Define a function to create a table
def create_table():
    try:
        # Define the CREATE TABLE SQL statement
        create_table_sql = """
            CREATE TABLE IF NOT EXISTS your_table_name (
                id SERIAL PRIMARY KEY,
                timestamp TIMESTAMP NOT NULL,
                client_id INT NOT NULL,
                protocol_id VARCHAR(16) NOT NULL
            );
        """

        # Execute the CREATE TABLE statement
        cur.execute(create_table_sql)
        conn.commit()

        print("Table 'your_table_name' created successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor
        cur.close()

# Call the create_table function to create the table
create_table()

# Get input values
timestamp_str = input("Enter timestamp (YYYY-MM-DD HH:MM:SS): ")
client_id = input("Enter client_id: ")
protocol_id = input("Enter protocol_id: ")

# Convert the timestamp string to a Python datetime object
try:
    timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
except ValueError:
    print("Invalid timestamp format. Use YYYY-MM-DD HH:MM:SS")
    conn.close()
    exit()

insert_query = """
    INSERT INTO your_table_name (timestamp, client_id, protocol_id)
    VALUES (%s, %s, %s);
"""

# Execute the query with the provided values
try:
    cur.execute(insert_query, (timestamp, client_id, protocol_id))
    conn.commit()  # Commit the transaction
    print("Entry added to the database.")
except Exception as e:
    print(f"Error: {e}")
    conn.rollback()  # Rollback the transaction in case of an error
finally:
    # Close the cursor and the database connection
    cur.close()
    conn.close()
