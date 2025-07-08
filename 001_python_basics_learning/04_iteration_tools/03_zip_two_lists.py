# 03_zip_two_lists.py
# Topic: Using zip() to loop over multiple lists together

names = ["Alice", "Bob", "Charlie", "Diana"]
scores = [85, 90, 78, 92]

print("Student Scores:")
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

pairs = list(zip(names, scores))
print(pairs)
