def outer():
    name = "Outer"

    def inner():
        print("Inner sees:", name)  # Enclosed scope

    inner()

outer()
