class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"

    @property
    def model(self):
        return self.__model 

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"
 

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
 
print("Is my_tesla an instance of ElectricCar?", isinstance(my_tesla,Car))
print("Is my_tesla an instance of ElectricCar?",isinstance(my_tesla,ElectricCar))
 
 
