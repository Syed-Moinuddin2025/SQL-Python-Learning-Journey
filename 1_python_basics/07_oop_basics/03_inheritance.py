class Car:
    def __init__(self, brand, model):  # ✅ Fixed double underscores
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):  # ✅ Fixed __init__
        super().__init__(brand, model)  # ✅ Fixed __init__ in super()
        self.battery_size = battery_size

# Create object
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# Display result
print(my_tesla.full_name())
print("Battery Size:", my_tesla.battery_size)
