import sqlite3

db_path = "/workspaces/E-Com/products.db"

conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Query to show the schema of the products table
cur.execute("PRAGMA table_info(products)")
columns = cur.fetchall()

print("Schema for 'products' table:")
for col in columns:
    print(f"{col[1]} ({col[2]})")

conn.close()