import time

# 🧠 Decorator that caches results
def cache(func):
    cache_value = {}

    def wrapper(*args):
        if args in cache_value:
            print(f"🧠 Returning cached result for {args}")
            return cache_value[args]
        print(f"💡 Computing result for {args}")
        result = func(*args)
        cache_value[args] = result
        return result

    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)  # Simulate delay
    return a + b

# 🚀 Run function calls
print(long_running_function(2, 3))  # 💡 Will compute
print(long_running_function(3, 5))  # 💡 Will compute
print(long_running_function(2, 3))  # 🧠 Will use cache
