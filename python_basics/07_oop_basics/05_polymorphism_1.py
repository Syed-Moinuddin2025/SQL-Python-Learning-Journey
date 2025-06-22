# Lesson 5: Polymorphism Example

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fuel_type(self):
        return "⛽ Uses Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "🔋 Runs on Electricity"

# Create objects
car1 = Car("Toyota", "Camry")
car2 = ElectricCar("Tesla", "Model Y", "75kWh")

# Polymorphic behavior
print(f"{car1.brand} {car1.model} → {car1.fuel_type()}")
print(f"{car2.brand} {car2.model} → {car2.fuel_type()}")
