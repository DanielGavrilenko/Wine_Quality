import sqlite3


def init_db():
    """
    Create request_column table
    """
    # Establish a connection to the SQLite database using a context manager
    with sqlite3.connect('requests.db') as conn:
        # Create the 'requests' table if it doesn't exist, with columns for different parameters.
        conn.execute('''CREATE TABLE IF NOT EXISTS requests (
                        id INTEGER PRIMARY KEY, 
                        fixed_acidity REAL, 
                        volatile_acidity REAL, 
                        citric_acid REAL, 
                        residual_sugar REAL, 
                        chlorides REAL, 
                        free_sulfur_dioxide REAL, 
                        total_sulfur_dioxide REAL, 
                        density REAL, 
                        pH REAL, 
                        sulphates REAL, 
                        alcohol REAL)''')


def save_request(input_model_data):
    """
    Save input_model_data to database.
    """
    with sqlite3.connect('requests.db') as conn:
        conn.execute("""
            INSERT INTO requests 
            (fixed_acidity, volatile_acidity, citric_acid, residual_sugar, 
            chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, 
            sulphates, alcohol)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
                     [input_model_data.get_attribute('fixed_acidity'),
                      input_model_data.get_attribute('volatile_acidity'),
                      input_model_data.get_attribute('citric_acid'),
                      input_model_data.get_attribute('residual_sugar'),
                      input_model_data.get_attribute('chlorides'),
                      input_model_data.get_attribute('free_sulfur_dioxide'),
                      input_model_data.get_attribute('total_sulfur_dioxide'),
                      input_model_data.get_attribute('density'),
                      input_model_data.get_attribute('pH'),
                      input_model_data.get_attribute('sulphates'),
                      input_model_data.get_attribute('alcohol')]
                     )


def load_requests():
    """
    Load all requests.
    """
    # Connect to the database using a context manager
    with sqlite3.connect('requests.db') as conn:
        cursor = conn.cursor()

        # Execute a SQL query to fetch all rows from the 'requests' table
        cursor.execute("SELECT * FROM requests")

        # Fetch all rows returned by the query
        rows = cursor.fetchall()

        # Return or use the fetched data as needed.
        return rows


def delete_requests():
    """
    Delete all requests
    """
    # Create a cursor object to execute SQL queries
    with sqlite3.connect('requests.db') as conn:
        cursor = conn.cursor()
        # Example: Drop a table
        drop_tabmle_query = "DROP TABLE IF EXISTS requests;"
        table_name = 'requests'
        cursor.execute(f'DELETE FROM {table_nae}')
