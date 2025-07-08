# 06_pass_statement.py
# Topic: Using pass inside loops or conditional blocks

# 🔹 Example 1: pass inside if-statement
print("Example 1: Using pass in if block")

x = 10

if x > 0:
    pass  # Later you can write something here
else:
    print("x is not positive")

print("Program continued after pass\n")

# 🔹 Example 2: pass inside for loop
print("Example 2: Loop runs but does nothing inside")

for i in range(3):
    pass  # Loop runs, but no action taken

print("Loop finished silently")
