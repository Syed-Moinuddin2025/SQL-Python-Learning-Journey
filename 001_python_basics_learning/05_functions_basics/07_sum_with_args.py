# 7. Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.
def sum_all(*args):
    print(args)                # Tuple print karta hai
    for i in args:
        print(i * 2)           # Har argument ka double print karta hai
    return sum(args)           # Total return karta hai

#print(sum_all(1, 2, 3))
total = sum_all(1, 2, 3,4,5)
print("Total =", total)

print("-------------*---------------------")

def total_sum(*args):
    return sum(args)

print("Total:", total_sum(10, 20, 30))
