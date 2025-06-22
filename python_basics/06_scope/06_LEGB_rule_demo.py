x = "global"

def outer():
    x = "enclosed"

    def inner():
        x = "local"
        print("Value is:", x)  # Prints local

    inner()

outer()
