class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

# Create objects
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
safari = Car("Tata", "Safari")

# Polymorphism in action
print(my_tesla.fuel_type())  # Output: Electric charge
print(safari.fuel_type())    # Output: Petrol or Diesel
