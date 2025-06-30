class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand    # private attribute
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Cars are means of transport."


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


# ✅ Creating car objects
car1 = Car("Toyota", "Fortuner")
car2 = Car("Tata", "Safari")
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# ✅ Display outputs
print("\n🚗 Car Details")
print("Car Name:", car1.full_name())
print("Fuel Type:", car1.fuel_type())

print("\n🔌 Electric Car Details")
print("Car Name:", my_tesla.full_name())
print("Fuel Type:", my_tesla.fuel_type())

# ✅ Static method usage
print("\n📘 General Description:", Car.general_description())

# ✅ Show total cars created
print(f"\n📊 Total Cars Created: {Car.total_car}")
