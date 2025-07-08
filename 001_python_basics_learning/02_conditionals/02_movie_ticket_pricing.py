# v2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.
# 02_ solution

age = 25
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
#price = price - 2
  price -= 2

#print(price)
print(f"Ticket price for you is ${price}")