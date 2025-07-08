def check_scope():
    if True:
        value = 100
    print("Inside function:", value)  # ✅ Accessible

check_scope()
# print(value)  # ❌ Error: value not defined outside function
