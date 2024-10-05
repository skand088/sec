import psycopg2
import sys


# Define your connection parameters
conn_params = {
    'dbname': 'mydb',
    'user': 'postgres',
    'password': 'Yuvrajsk6-',
    'host': 'localhost',
    'port': '5432'
}

# Read the .sql file
with open(r'C:\Users\skand\OneDrive\sec_programming\sec\database.sql', 'r') as file:
    sql_commands = file.read()

# Establish the connection
try:
    conn = psycopg2.connect(**conn_params)
    print("Connection successful")
except Exception as e:
    print(f"Error connecting to the database: {e}")

# Create a cursor object
cur = conn.cursor()

# Execute the SQL commands
try:
    cur.execute(sql_commands)
    conn.commit()  # Commit the transaction
    print("SQL file executed successfully")
except Exception as e:
    conn.rollback()  # Rollback the transaction on error
    print(f"Error executing SQL file: {e}")

# Close the cursor and connection
cur.close()
conn.close()
