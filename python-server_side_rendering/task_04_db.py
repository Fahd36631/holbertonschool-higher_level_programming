#!/usr/bin/env python3
"""
Task 4: Extending Dynamic Data Display to Include SQLite in Flask
"""

import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_products():
    """Read products from JSON file."""
    try:
        with open('products.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def read_csv_products():
    """Read products from CSV file."""
    products = []
    try:
        with open('products.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert id and price to appropriate types
                product = {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                products.append(product)
    except FileNotFoundError:
        return []
    except (ValueError, KeyError):
        return []
    
    return products


def read_sql_products():
    """Read products from SQLite database."""
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        
        for row in rows:
            product = {
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            }
            products.append(product)
        
        conn.close()
    except sqlite3.Error:
        return []
    except FileNotFoundError:
        return []
    
    return products


@app.route('/products')
def products():
    """Display products from JSON, CSV, or SQLite based on query parameter."""
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    
    # Handle invalid source
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")
    
    # Read products based on source
    if source == 'json':
        all_products = read_json_products()
    elif source == 'csv':
        all_products = read_csv_products()
    else:  # source == 'sql'
        all_products = read_sql_products()
    
    # Filter by id if provided
    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in all_products if p.get('id') == product_id]
            if not filtered_products:
                return render_template('product_display.html', error="Product not found")
            products_to_display = filtered_products
        except ValueError:
            return render_template('product_display.html', error="Product not found")
    else:
        products_to_display = all_products
    
    return render_template('product_display.html', products=products_to_display)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
