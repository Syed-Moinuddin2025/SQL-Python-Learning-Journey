# 07_file_readline.py
# Topic: Reading lines from a file using open(), readline(), and for-loop (with path handling)

import os

# ✅ Safely build file path
file_path = os.path.join("04_iteration_tools", "sample.txt")

# 🔹 Read first line
print("Reading one line using readline():")
with open(file_path, "r") as file:
    first_line = file.readline()
    print("First Line:", first_line.strip())

print("\n")

# 🔹 Read all lines using loop
print("Reading all lines using a loop:")
with open(file_path, "r") as file:
    for line in file:
        print(line.strip())

print("\n")

# 🔹 Safe method already used with 'with open()'
print("Reading safely with 'with open() as' block:")
with open(file_path, "r") as f:
    for line in f:
        print(line.strip())
