# 2. Class Method and Self
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).

# Lesson 2: Class Method and self

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):  # Class method using self
        return f"{self.brand} {self.model}"

# Create object
my_car = Car("Toyota", "Corolla")

# Call the method
print("Full name of the car is:", my_car.full_name())
