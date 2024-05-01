import sqlite3

# Connect to the SQLite database (create it if it doesn't exist)
conn = sqlite3.connect('meddb.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table for users
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    address TEXT NOT NULL,
                    password TEXT NOT NULL
                 )''')

# Create a table for medicines
cursor.execute('''CREATE TABLE IF NOT EXISTS medicines (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    description TEXT
                 )''')

# Create a table for dealers
cursor.execute('''CREATE TABLE IF NOT EXISTS dealers (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    location TEXT NOT NULL
                 )''')

# Create a table for sellers
cursor.execute('''CREATE TABLE IF NOT EXISTS sellers (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    location TEXT NOT NULL
                 )''')

# Commit changes and close the connection
conn.commit()
conn.close()
