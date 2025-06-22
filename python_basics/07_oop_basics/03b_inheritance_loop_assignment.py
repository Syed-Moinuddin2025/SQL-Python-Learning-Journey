# 🎯 Task:
# 1.	Create a class ElectricCar that inherits from Car.  Make a list of 3 to 5 ElectricCar objects. Use a for loop to display all car details using a method.

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
        print("🚗 Car Info")
        print(f"Name         : {self.full_name()}")
        print(f"Battery Size : {self.battery_size}")
        print("-" * 30)

# ✅ Step 1: Create a list of ElectricCar objects
car_list = [
    ElectricCar("Tesla", "Model 3", "75kWh"),
    ElectricCar("Nissan", "Leaf", "40kWh"),
    ElectricCar("Hyundai", "Kona", "64kWh"),
    ElectricCar("BMW", "i3", "42kWh"),
    ElectricCar("MG", "ZS EV", "50kWh")
]

# ✅ Step 2: Loop through list and display each car
for car in car_list:
    car.display_info()
