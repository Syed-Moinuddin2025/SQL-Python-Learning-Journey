import os
import json

# 🎯 Safely get full path of menu.json
def load_menu():
    base_path = os.path.dirname(__file__)
    menu_path = os.path.join(base_path, "menu.json")
    try:
        with open(menu_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Menu file not found!")
        exit()

# 🧾 Show menu from loaded JSON
def show_menu(menu):
    for category, items in menu.items():
        print(f"\n🍽️ {category}")
        for item in items:
            print(f"  {item['id']}. {item['name']} - ₹{item['price']}")

# 🛒 Add item to the order
def add_item_to_order(menu, order, item_id):
    for category_items in menu.values():
        for item in category_items:
            if item['id'] == item_id:
                order.append(item)
                print(f"✅ Added: {item['name']} - ₹{item['price']}")
                return
    print("❌ Item ID not found!")

# 💵 Show total bill
def show_bill(order):
    print("\n🧾 Your Order Summary:")
    total = 0
    for item in order:
        print(f"  - {item['name']} - ₹{item['price']}")
        total += item['price']
    print(f"💰 Total: ₹{total}")

# 🚀 Main app loop
def main():
    menu = load_menu()
    order = []

    while True:
        print("\n🔘 1. Show Menu")
        print("🔘 2. Add Item to Order")
        print("🔘 3. Show Bill")
        print("🔘 4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            show_menu(menu)
        elif choice == '2':
            try:
                item_id = int(input("Enter item ID to add: "))
                add_item_to_order(menu, order, item_id)
            except ValueError:
                print("❗ Please enter a valid number.")
        elif choice == '3':
            show_bill(order)
        elif choice == '4':
            print("👋 Thank you for visiting Pizza Hut!")
            break
        else:
            print("❗ Invalid choice, try again.")

# ▶️ Start the app
if __name__ == "__main__":
    main()
