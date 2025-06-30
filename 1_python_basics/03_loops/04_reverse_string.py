# 4. Reverse a String
# Problem: Reverse a string using a loop.

input_str = "Python"
reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str
print(reversed_str)