# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.
input_str = "googlethis"
for char in input_str :
    print(char)
    if input_str.count(char) == 1:
        print("First non-repeated character is:", char)
        break