# 3. Polymorphism in Functions
# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def multiply(a, b):
    """Multiplies numbers or repeats a string."""
    return a * b

# Example usages:
print(multiply(5, 3))         # 15 → number * number
print(multiply("Hi ", 3))     # "Hi Hi Hi " → string * number
print(multiply(3, "Hello "))  # "Hello Hello Hello " → number * string
