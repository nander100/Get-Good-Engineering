import sqlite3

connection = sqlite3.connect('example.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')
print(connection)

# Insert data
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ("Alice", 30))  # Use %s for MySQL/PostgreSQL

# Fetch data
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)