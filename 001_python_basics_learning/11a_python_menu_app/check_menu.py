import os
import json

# 🎯 Safely get full path of menu.json
def load_menu():
    base_path = os.path.dirname(__file__)
    menu_path = os.path.join(base_path, "menu1.json")
    try:
        with open(menu_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Menu file not found!")
        exit()


# Display menu with numbering
def display_menu(menu_items, columns=4):
    print("\n📋 MENU:")
    items = list(menu_items.items())
    max_len = max(len(f"{i+1}. {item} - ${price:.2f}") for i, (item, price) in enumerate(items))
    row_format = ("{:<" + str(max_len + 5) + "}") * columns

    for i in range(0, len(items), columns):
        row = []
        for j in range(columns):
            if i + j < len(items):
                idx = i + j + 1
                item, price = items[i + j]
                row.append(f"{idx}. {item} - ${price:.2f}")
            else:
                row.append("")  # Empty for alignment
        print(row_format.format(*row))

def get_item_by_number(menu, number):
    items = list(menu.items())
    if 1 <= number <= len(items):
        return items[number - 1]
    return None, None

# Take multiple item orders
def take_order(menu):
    order = {}
    while True:
        try:
            choice = int(input("\nEnter item number (0 to finish): "))
            if choice == 0:
                break

            item, price = get_item_by_number(menu, choice)
            if not item:
                print("⚠️ Invalid item number.")
                continue

            quantity = int(input(f"Enter quantity for {item}: "))
            if quantity <= 0:
                print("⚠️ Quantity must be at least 1.")
                continue

            if item in order:
                order[item]["quantity"] += quantity
            else:
                order[item] = {"price": price, "quantity": quantity}
        except ValueError:
            print("⚠️ Please enter valid numbers.")
    return order

# Print final bill
def print_bill(order):
    if not order:
        print("\n🛒 No items ordered.")
        return

    print("\n🧾 Final Bill")
    print("-" * 30)
    total = 0
    for item, details in order.items():
        price = details["price"]
        qty = details["quantity"]
        item_total = price * qty
        total += item_total
        print(f"{item} x {qty} = ${item_total:.2f}")
    print("-" * 30)
    print(f"🟢 Total: ${total:.2f}")
    print("🎉 Thank you for your order! 🎉")

# Main flow
def main():
    menu = load_menu()
    if not menu:
        return

    display_menu(menu)
    order = take_order(menu)
    print_bill(order)

if __name__ == "__main__":
    main()