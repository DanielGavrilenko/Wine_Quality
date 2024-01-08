import sqlite3

# Connect to a database (creates a new file if not exists)
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a SQL query to create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Insert data into the table
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('John Doe', 25))

# Commit changes and close the connection
conn.commit()
conn.close()

# To fetch data
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
