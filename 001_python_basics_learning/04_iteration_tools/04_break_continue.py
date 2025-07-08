# 04_break_continue.py
# Topic: Using break and continue inside loops

# 🔴 Example 1: break
print("Example 1: break - stop loop when number is 5")

for i in range(1, 11):
    if i == 5:
        print("Breaking the loop at", i)
        break
    print("Number:", i)

print("\n")

# 🟡 Example 2: continue
print("Example 2: continue - skip number 5")

for i in range(1, 11):
    if i == 5:
        print("Skipping", i)
        continue
    print("Number:", i)
