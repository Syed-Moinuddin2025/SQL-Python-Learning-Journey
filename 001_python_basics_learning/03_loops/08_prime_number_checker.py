# 8. Prime Number Checker
# Problem: Check if a number is prime.

number = 28
is_prime = True

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
else:
    is_prime = False

if is_prime:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")

 