from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def get_db_connection():
    connection = sqlite3.connect('../database/products.db')
    connection.row_factory = sqlite3.Row
    return connection


@app.route('/')
def index():
    connection = get_db_connection()
    products = connection.execute('SELECT * FROM products').fetchall()
    connection.close()

    return render_template('index.html', products=products)


@app.route('/search', methods=['GET'])
def search():
    min_price = request.args.get('min_price', default=0, type=float)

    connection = get_db_connection()
    query = 'SELECT * FROM products WHERE Price >= ?'
    products = connection.execute(query, (min_price,)).fetchall()
    connection.close()

    return render_template('index.html', products=products, min_price=min_price)


if __name__ == '__main__':
    app.run(debug=True)
