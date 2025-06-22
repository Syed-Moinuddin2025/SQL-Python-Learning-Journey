# 🔋 First Parent Class
class Battery:
    def battery_info(self):
        return "Battery capacity: 85kWh"

# 🛠️ Second Parent Class
class Engine:
    def engine_info(self):
        return "Electric engine with dual motors"

# 🚗 Child Class — Inherits from Battery & Engine
class ElectricCar(Battery, Engine):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def car_info(self):
        return f"{self.brand} {self.model}"
# Create object of ElectricCar
my_ev = ElectricCar("Tesla", "Model S")

# Call all methods
print("🚗 Car Info:", my_ev.car_info())
print("🔋", my_ev.battery_info())
print("🛠️", my_ev.engine_info())

 
 
 
