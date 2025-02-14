import mysql.connector
from mysql.connector import Error

# Database connection details for Azure MySQL
DB_CONFIG = {
    "host": "priyacompanydb.mysql.database.azure.com",
    "user": "priya",  # REMOVE '@priyacompanydb'
    "password": "Admin@1234",
    "database": "priyacompanydb",
    "port": 3306  # ADD this explicitly
}


def execute_sql_script(filename):
    connection = None
    try:
        # Establish connection
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        # Read SQL script
        with open(filename, 'r') as file:
            sql_commands = file.read().split(";")  # Split script into individual queries
        
        # Execute each SQL command safely
        for command in sql_commands:
            command = command.strip()
            if command:
                try:
                    cursor.execute(command)
                except mysql.connector.Error as err:
                    # Skip duplicate column error (Error Code: 1060)
                    if err.errno == 1060:
                        print(f"Skipping duplicate column error: {err}")
                    else:
                        raise err

        # Commit changes
        connection.commit()
        print("SQL script executed successfully.")

    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("🔗 Connection closed.")

# Run the script
if __name__ == "__main__":
    execute_sql_script("schema_changes.sql")
