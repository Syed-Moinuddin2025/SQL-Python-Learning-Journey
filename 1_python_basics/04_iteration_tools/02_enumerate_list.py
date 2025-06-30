# 02_enumerate_list.py
# Topic: Using enumerate() to loop with index and value

fruits = ["apple", "banana", "mango", "grapes"]

# print("Using enumerate():")

for index, fruit in enumerate(fruits):
    print(f"Index {index} ➝ {fruit}")
print()
for i in range(len(fruits)):
    print( i, fruits[i])
print()
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
