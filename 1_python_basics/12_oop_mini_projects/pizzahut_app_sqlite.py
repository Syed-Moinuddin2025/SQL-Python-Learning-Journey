import os
import json
import sqlite3
from datetime import datetime
import csv

# ✅ Step 1: Get current script's directory
base_path = os.path.dirname(os.path.abspath(__file__))
menu_path = os.path.join(base_path, "menu1.json")
db_path = os.path.join(base_path, "pizzahut_sales.db")

# ✅ Step 2: Load menu from menu1.json
def load_menu():
    try:
        with open(menu_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ menu1.json file not found.")
        return []

# ✅ Step 3: Initialize SQLite database
def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
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
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales_summary (
            date TEXT PRIMARY KEY,
            total_orders INTEGER,
            total_amount INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# ✅ Step 4: Save order to database
def save_order(customer, order_items):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    date_str = datetime.now().strftime("%Y-%m-%d")
    total_amount = 0

    for item in order_items:
        name = item["name"]
        quantity = item["quantity"]
        price = item["price"]
        total = quantity * price
        total_amount += total

        cursor.execute('''
            INSERT INTO bills (customer, item, quantity, price, total, date)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (customer, name, quantity, price, total, date_str))

    # Update or insert into summary table
    cursor.execute('SELECT * FROM sales_summary WHERE date = ?', (date_str,))
    existing = cursor.fetchone()
    if existing:
        cursor.execute('''
            UPDATE sales_summary
            SET total_orders = total_orders + 1,
                total_amount = total_amount + ?
            WHERE date = ?
        ''', (total_amount, date_str))
    else:
        cursor.execute('''
            INSERT INTO sales_summary (date, total_orders, total_amount)
            VALUES (?, ?, ?)
        ''', (date_str, 1, total_amount))

    conn.commit()
    conn.close()

# ✅ Step 5: Export to CSV
def export_sales_to_csv(date_str):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bills WHERE date = ?", (date_str,))
    rows = cursor.fetchall()

    if rows:
        csv_file = os.path.join(base_path, f"sales_summary_{date_str}.csv")
        with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Customer", "Item", "Quantity", "Price", "Total", "Date"])
            writer.writerows(rows)
        print(f"📝 Sales exported to {csv_file}")
    else:
        print("📭 No sales to export today.")

    conn.close()

# ✅ Step 6: Main program
def main():
    init_db()
    menu = load_menu()
    if not menu:
        return

    print("🍕 Welcome to Pizza Hut!")
    customer = input("Enter your name: ").strip()
    order = []

    # 🎯 Filter menu
    print("\n🎯 Do you want to filter menu by category?")
    print("1. Show All\n2. Pizza Only\n3. Burger Only\n4. Cold Drink Only\n5. Sides Only\n6. Salads Only\n7. Desserts Only")
    choice = input("Enter your choice (1–7): ")

    filter_map = {
        "2": "Pizza",
        "3": "Burger",
        "4": "Cold Drink",
        "5": "Sides",
        "6": "Salad",
        "7": "Dessert"
    }
    selected_category = filter_map.get(choice)

    emoji_map = {
        "Pizza": "🍕",
        "Burger": "🍔",
        "Cold Drink": "🥤",
        "Sides": "🍟",
        "Salad": "🥗",
        "Dessert": "🍰"
    }

    print("\n📋 Menu:")
    categories_to_show = [selected_category] if selected_category else sorted(set(item["category"] for item in menu))

    for cat in categories_to_show:
        print(f"\n{emoji_map.get(cat, '📦')} {cat.upper()}S")
        for item in menu:
            if item["category"] == cat:
                print(f"  {item['id']:>2}. {item['name']:<20} ₹{item['price']}")

    while True:
        try:
            item_id = int(input("Enter item ID (0 to finish): "))
            if item_id == 0:
                break
            quantity = int(input("Enter quantity: "))
            item = next((i for i in menu if i["id"] == item_id), None)
            if item:
                order.append({
                    "name": item["name"],
                    "price": item["price"],
                    "quantity": quantity
                })
                print(f"✅ Added {quantity} x {item['name']} to your order")
            else:
                print("❌ Invalid item ID")
        except ValueError:
            print("❌ Please enter valid numbers.")

    if order:
        print(f"\n🧾 Bill for {customer}")
        print("-" * 40)
        total_amount = 0
        for item in order:
            line_total = item["quantity"] * item["price"]
            print(f"{item['name']:<20} x{item['quantity']}   ₹{line_total}")
            total_amount += line_total
        print("-" * 40)
        print(f"Total Amount: ₹{total_amount}")

        save_order(customer, order)
        print("📦 Bill and summary saved to SQLite3 database.")
        export_sales_to_csv(datetime.now().strftime("%Y-%m-%d"))
    else:
        print("❌ No items selected.")

if __name__ == "__main__":
    main()
