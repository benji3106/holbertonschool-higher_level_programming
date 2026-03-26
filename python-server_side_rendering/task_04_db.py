#!/usr/bin/python3
"""Flask app to display products from JSON, CSV, or SQLite"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json_file(filename):
    """Read products from a JSON file"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception:
        return []


def read_csv_file(filename):
    """Read products from a CSV file"""
    products = []

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except Exception:
        return []

    return products


def read_sqlite_file(filename):
    """Read products from a SQLite database"""
    products = []

    try:
        conn = sqlite3.connect(filename)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            products.append({
                "id": row["id"],
                "name": row["name"],
                "category": row["category"],
                "price": row["price"]
            })
    except Exception:
        return []

    return products


@app.route('/products')
def products():
    """Display products from JSON, CSV, or SQLite"""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        products_list = read_json_file('products.json')
    elif source == 'csv':
        products_list = read_csv_file('products.csv')
    elif source == 'sql':
        products_list = read_sqlite_file('products.db')
    else:
        return render_template(
            'product_display.html',
            error="Wrong source",
            products=[]
        )

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html',
                error="Product not found",
                products=[]
            )

        filtered_products = []

        for product in products_list:
            if product.get("id") == product_id:
                filtered_products.append(product)

        if not filtered_products:
            return render_template(
                'product_display.html',
                error="Product not found",
                products=[]
            )

        return render_template(
            'product_display.html',
            products=filtered_products,
            error=None
        )

    return render_template(
        'product_display.html',
        products=products_list,
        error=None
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
