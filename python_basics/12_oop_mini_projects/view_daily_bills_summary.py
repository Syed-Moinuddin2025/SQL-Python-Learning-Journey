import sqlite3
from tabulate import tabulate
from datetime import datetime
import os

# ✅ Set path to SQLite3 database
base_path = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_path, "pizzahut_sales.db")

# ✅ Show today's bill summary
def show_daily_bills_summary():
    date_str = str(datetime.now().date())

    # Connect to DB
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 📋 Fetch all bills from today
    cursor.execute('''
        SELECT customer, item, quantity, price, total
        FROM bills
        WHERE date = ?
    ''', (date_str,))
    rows = cursor.fetchall()

    if not rows:
        print(f"📭 No bills found for {date_str}")
        return

    headers = ["Customer", "Item", "Qty", "Price", "Total"]
    print(f"\n📊 Bills Summary for {date_str}:\n")
    print(tabulate(rows, headers=headers, tablefmt="grid"))

    # 📌 Fetch sales summary from summary table
    cursor.execute('''
        SELECT total_orders, total_amount
        FROM sales_summary
        WHERE date = ?
    ''', (date_str,))
    summary = cursor.fetchone()
    if summary:
        print(f"\n🧾 Total Orders: {summary[0]}")
        print(f"💰 Total Sales: ₹{summary[1]}")

    conn.close()

if __name__ == "__main__":
    show_daily_bills_summary()
