# 01_range_basics.py
# Topic: Using range() in Python for looping

# 1️⃣ Basic range: range(stop)
print("1. range(5) ➝ from 0 to 4")
for i in range(5):
    print(i)  # Output: 0 1 2 3 4

print("\n2. range(1, 6) ➝ from 1 to 5")
# 2️⃣ range(start, stop)
for i in range(1, 6):
    print(i)  # Output: 1 2 3 4 5

print("\n3. range(2, 11, 2) ➝ even numbers between 2 and 10")
# 3️⃣ range(start, stop, step)
for i in range(2, 11, 2):
    print(i)  # Output: 2 4 6 8 10
