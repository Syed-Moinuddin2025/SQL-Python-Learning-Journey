# 5. Default Parameter Value
# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.


def greet(name="Guest"):
    #Greets the user with a default name if none is provided.
    print(f"Hello, {name}!")

# Example usage:
greet("Kohli")      # Output: Hello, name!
#greet()            # Output: Hello, Guest!
