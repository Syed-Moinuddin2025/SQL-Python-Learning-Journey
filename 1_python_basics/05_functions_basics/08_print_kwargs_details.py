# 8. Function with ** kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format # key: value.

def print_kwargs ( ** kwargs):
    for key, value in kwargs. items () :
        print(f"{key}: {value}")

print_kwargs (name="shaktiman", power="lazer",enemy = "Dr. Jackaal")
print("*************************")
print_kwargs(name="Syed", age=25, country="India") 
print("------------------------------")
print_kwargs(language="Python", level="Beginner", enrolled=True)