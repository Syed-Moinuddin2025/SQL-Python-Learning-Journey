# 1. Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

# Basic Class and Object Example

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")

# Creating an object of Car
my_car = Car("Toyota", "Corolla")

# Display car information
#my_car.display_info()
print(my_car.brand)
print(my_car.model)
# You can also access individual attributes
#print("Accessing directly:", my_car.brand, my_car.model)
