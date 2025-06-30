# 05_loop_with_else.py
# Topic: Using else with loops (for...else, while...else)

# 🔹 Example 1: for...else - search with no break
print("Searching for 7 in [1, 2, 3, 4, 5]:")

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 7:
        print("Found 7!")
        break
else:
    print("7 not found in the list")  # else runs only if loop completes without break

print("\n")

# 🔹 Example 2: while...else - countdown with no interruption
print("Countdown:")

i = 3
while i > 0:
    print(i)
    i -= 1
else:
    print("Blast off!")  # runs after while loop finishes normally
