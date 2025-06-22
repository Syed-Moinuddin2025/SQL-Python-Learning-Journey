# Personal Information Class Example

class Person:
    def __init__(self, first_name, last_name, age, contact_number, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.contact_number = contact_number
        self.city = city

    def display_info(self):
        print("📋 Personal Information")
        print(f"Name          : {self.first_name} {self.last_name}")
        print(f"Age           : {self.age} years")
        print(f"Contact Number: {self.contact_number}")
        print(f"City          : {self.city}")

# Create an object of Person
person1 = Person("Syed", "Moin", 25, "9876543210", "Hyderabad")

# Display the info
person1.display_info()
