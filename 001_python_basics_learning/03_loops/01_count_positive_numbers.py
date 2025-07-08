# v1. Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positive_number = 0
negative_number = 0

for num in numbers :
    if num >0:
        positive_number +=1
    if num <0:
        negative_number +=1


print(f"Here is result: Positive numbers = {positive_number} & Negative numbers = {negative_number}")




