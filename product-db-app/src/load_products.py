import sqlite3
import csv

db_path = "products.db"
csv_path = "/workspaces/E-Com/products.csv"  # Corrected path

# Connect to SQLite database
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Drop the old products table if it exists
cur.execute("DROP TABLE IF EXISTS products")

# Create table matching CSV columns
cur.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    cost REAL,
    category TEXT,
    name TEXT,
    brand TEXT,
    retail_price REAL,
    department TEXT,
    sku TEXT,
    distribution_center_id INTEGER
)
""")

# Read CSV and insert data
with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cur.execute("""
            INSERT INTO products (id, cost, category, name, brand, retail_price, department, sku, distribution_center_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            row['id'],
            row['cost'],
            row['category'],
            row['name'],
            row['brand'],
            row['retail_price'],
            row['department'],
            row['sku'],
            row['distribution_center_id']
        ))

conn.commit()

# Verify data: print first 5 rows
cur.execute("SELECT * FROM products LIMIT 5")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()