# 9. Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit.
def even_generator(limit) :
    for i in range(2, limit + 1, 2):
        yield i

for num in even_generator(10):
    print(num)

print("----------------------Next-----------------------------")

def even_numbers(limit):
    for num in range(1, limit + 1):
        if num % 2 == 0:
            yield num 

for num in even_numbers(10):
        print(num)
