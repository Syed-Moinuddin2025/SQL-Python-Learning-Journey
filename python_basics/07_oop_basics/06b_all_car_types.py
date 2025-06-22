# 🚗 ElectricCar Class with Color (No list used)

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size, color):
        super().__init__(brand, model)
        self.battery_size = battery_size
        self.color = color

    def display_info(self):
        print(f"🚘 {self.full_name()} | 🔋 {self.battery_size} | 🎨 Color: {self.color}")

# ✅ Create and display cars one by one
car1 = ElectricCar("Tesla", "Model S", "85kWh", "Red")
car1.display_info()

car2 = ElectricCar("Tata", "Nexon EV", "40kWh", "Blue")
car2.display_info()

car3 = ElectricCar("Hyundai", "Kona", "64kWh", "White")
car3.display_info()

car4 = ElectricCar("MG", "ZS EV", "50kWh", "Black")
car4.display_info()

car5 = ElectricCar("BYD", "Atto 3", "60kWh", "Silver")
car5.display_info()
