#!/usr/bin/env python3
"""
Task 3: Displaying Data from JSON or CSV Files in Flask
"""

import json
import csv
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


@app.route('/products')
def products():
    """Display products from JSON or CSV based on query parameter."""
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    
    # Handle invalid source
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    
    # Read products based on source
    if source == 'json':
        all_products = read_json_products()
    else:  # source == 'csv'
        all_products = read_csv_products()
    
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
