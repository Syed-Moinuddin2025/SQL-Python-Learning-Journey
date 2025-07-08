# 🔧 Decorator to print function name and its arguments
def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"calling: {func.__name__} with args: {args_value} and kwargs: {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

# 🧪 Testing with a simple function
@debug
def hello():
    print("hello")

# 🔽 Testing with function having arguments
@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

# 🚀 Run functions
hello()
greet("chai", greeting="code")
 