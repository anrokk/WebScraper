import sqlite3
import json
from pathlib import Path

connection = sqlite3.connect('products.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        Title TEXT,
        Price REAL,
        Picture_href TEXT
    )
''')

with open(Path(__file__).parent.parent / 'scraper' / 'products.json', encoding='utf-8') as file:
    data = json.load(file)

for product in data:

    price_str = product['Price'].replace(" €", "").replace(",", ".")

    price = float(price_str)

    cursor.execute('''
        INSERT INTO products (Title, Price, Picture_href)
        VALUES (?, ?, ?)
    ''', (product['Title'], price, product['Picture href']))

connection.commit()
connection.close()
