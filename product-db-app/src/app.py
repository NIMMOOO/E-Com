from flask import Flask, jsonify
from flask_cors import CORS

import sqlite3

app = Flask(__name__)
CORS(app)

DB_PATH = "/workspaces/E-Com/products.db"  # <-- Add leading slash

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/products', methods=['GET'])
def list_products():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return jsonify([dict(row) for row in products])

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = ?', (product_id,)).fetchone()
    conn.close()
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(dict(product))

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Products API"}), 200

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(400)
def bad_request(e):
    return jsonify({'error': 'Invalid request'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
fetch("https://symmetrical-enigma-7jppp4rp95qcrvr-5000.app.github.dev/api/products")
  .then(res => res.json())
  .then(data => {
    console.log("✅ Data from API:", data);
  })
  .catch(err => console.error("❌ Fetch error:", err));
