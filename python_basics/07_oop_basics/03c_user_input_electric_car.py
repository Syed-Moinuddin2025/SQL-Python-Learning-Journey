# 🚗 ElectricCar Class with User Input

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def display_info(self):
        print("\n✅ Car Information Entered:")
        print(f"Brand & Model : {self.full_name()}")
        print(f"Battery Size  : {self.battery_size}")
        print("-" * 30)

# 📥 Taking user input
print("🔧 Please enter electric car details")
brand = input("Enter car brand        : ")
model = input("Enter car model        : ")
battery = input("Enter battery size (kWh): ")

# ✅ Create object
user_car = ElectricCar(brand, model, battery)

# 🔍 Display info
user_car.display_info()
