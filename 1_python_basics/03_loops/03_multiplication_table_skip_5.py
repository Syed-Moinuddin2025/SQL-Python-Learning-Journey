#  3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number = 5

for i in range(1, 11):
    if i ==5:
        continue
    print(number , 'x' , i , '=', number * i)

    # print(f"{number} x {i} = {number * i}")
     
number = 5

print("Without f-string:")
for i in range(1, 6):
    print(number, 'x', i, '=', number * i)

print("\nWith f-string:")
for i in range(1, 6):
    print(f"{number} x {i} = {number * i}")