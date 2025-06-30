import json
import os
import csv
from datetime import datetime

# ✅ Get current script's directory
base_path = os.path.dirname(os.path.abspath(__file__))
menu_path = os.path.join(base_path, "pizzahut_menu.json")

# ✅ Load Menu
def load_menu():
    try:
        with open(menu_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Menu file not found.")
        return []

# ✅ Define Classes
class FoodItem:
    def __init__(self, item_id, name, price, category):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.category = category

class Order:
    def __init__(self, customer_name):
        self.customer = customer_name
        self.items = []

    def add_item(self, food_item, quantity):
        self.items.append((food_item, quantity))
        print(f"✅ Added {quantity} x {food_item.name} to your order")

    def show_bill(self):
        print(f"\n🧾 Bill for {self.customer}")
        print("-" * 40)
        total = 0
        for food_item, qty in self.items:
            cost = food_item.price * qty
            print(f"{food_item.name:<20} x{qty:<3} ₹{cost}")
            total += cost
        print("-" * 40)
        print(f"Total Amount: ₹{total}")
        return total

# ✅ Save Bills in One CSV File
def save_bill_as_csv(order):
    date_str = str(datetime.now().date())
    csv_filename = os.path.join(base_path, f"daily_bills_{date_str}.csv")
    file_exists = os.path.exists(csv_filename)

    with open(csv_filename, "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["Customer", "Item", "Quantity", "Price", "Total"])
        for item, qty in order.items:
            total = item.price * qty
            writer.writerow([order.customer, item.name, qty, item.price, total])
    print(f"📄 Bill saved in CSV: daily_bills_{date_str}.csv")

# ✅ Update Daily Sales Summary
def update_sales_summary(order, total_amount):
    date_str = str(datetime.now().date())
    summary_file = os.path.join(base_path, f"sales_summary_{date_str}.json")

    if os.path.exists(summary_file):
        with open(summary_file, "r", encoding="utf-8") as f:
            summary = json.load(f)
    else:
        summary = {"total_orders": 0, "total_amount": 0}

    summary["total_orders"] += 1
    summary["total_amount"] += total_amount

    with open(summary_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4)
    print(f"📊 Sales summary updated for {date_str}")

# ✅ Main Function
def main():
    menu_data = load_menu()
    if not menu_data:
        return

    menu = [FoodItem(**item) for item in menu_data]

    print("\n📋 Pizza Hut Menu:")
    for item in menu:
        print(f"{item.item_id}. {item.name} - ₹{item.price} ({item.category})")

    customer_name = input("\nEnter customer name: ")
    order = Order(customer_name)

    while True:
        try:
            item_id = int(input("Enter item ID (0 to finish): "))
            if item_id == 0:
                break
            quantity = int(input("Enter quantity: "))
            matched_items = [item for item in menu if item.item_id == item_id]
            if matched_items:
                order.add_item(matched_items[0], quantity)
            else:
                print("❌ Invalid item ID.")
        except ValueError:
            print("❌ Invalid input. Please enter numbers.")

    if order.items:
        total_amount = order.show_bill()
        save_bill_as_csv(order)
        update_sales_summary(order, total_amount)
    else:
        print("🛑 No items were added to the order.")

if __name__ == "__main__":
    main()