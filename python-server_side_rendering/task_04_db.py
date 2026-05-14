#!/usr/bin/python3

import json
import csv
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json') as f:
        data = json.load(f)
    return render_template('items.html', items=data["items"])

def read_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def read_csv_file(filename):
    products = []
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["price"] = float(row["price"])
            row["id"] = int(row["id"])
            products.append(row)
    return products

def read_sql_data(product_id=None):
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        
        if product_id:
            cursor.execute("SELECT id, name, category, price FROM Products WHERE id = ?", (product_id,))
            result = cursor.fetchone()
            if result:
                products.append({
                    "id": result[0],
                    "name": result[1],
                    "category": result[2],
                    "price": result[3]
                })
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")
            results = cursor.fetchall()
            for row in results:
                products.append({
                    "id": row[0],
                    "name": row[1],
                    "category": row[2],
                    "price": row[3]
                })
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
    elif source == 'sql':
        products = read_sql_data(product_id=int(product_id) if product_id else None)
    else:
        return render_template('product_display.html', error="Wrong source specified.")
    if product_id and not products:
        return render_template('product_display.html', error="Product not found.")
    return render_template('product_display.html', products=products)
if __name__ == '__main__':
    app.run(debug=True, port=5000)
