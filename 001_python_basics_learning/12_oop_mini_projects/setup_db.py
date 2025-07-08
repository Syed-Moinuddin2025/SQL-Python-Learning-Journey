import sqlite3
import os

# ✅ Get database path in current folder
base_path = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_path, "pizzahut_sales.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# ✅ Create 'bills' table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS bills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer TEXT,
        item TEXT,
        quantity INTEGER,
        price INTEGER,
        total INTEGER,
        date TEXT
    )
''')

# ✅ Create 'sales_summary' table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales_summary (
        date TEXT PRIMARY KEY,
        total_orders INTEGER,
        total_amount INTEGER
    )
''')

conn.commit()
conn.close()
print("✅ Tables created successfully.")
print(f"Using DB at: {db_path}")