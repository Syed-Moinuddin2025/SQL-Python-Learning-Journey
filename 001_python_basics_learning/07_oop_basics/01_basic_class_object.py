# Define the Car class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")

# Create an object (instance) of Car
my_car = Car("Toyota", "Corolla")

# Call the method to display car info
my_car.display_info()
