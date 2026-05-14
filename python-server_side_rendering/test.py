#!/usr/bin/python3
import sqlite3

def create_database():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Create the Products table if it does not already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Insert initial data
    cursor.execute('''
        INSERT OR IGNORE INTO Products (id, name, category, price)
        VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    
    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

# Execute the function to set up the database
if __name__ == '__main__':
    create_database()