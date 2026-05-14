#!/usr/bin/python3

import json
import csv

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

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
    else:
        return render_template('product_display.html', error="Wrong source specified.")

    if product_id:
        try:
            product_id = int(product_id)
            products = [product for product in products if product["id"] == product_id]
            if not products:
                return render_template('product_display.html', error="Product not found.")
        except ValueError:
            return render_template('product_display.html', error="Invalid product ID.")
    
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
