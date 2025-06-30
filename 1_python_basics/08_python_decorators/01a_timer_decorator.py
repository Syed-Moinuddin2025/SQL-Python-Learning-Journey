import time

# ✅ Decorator that measures execution time
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()              # Record start time
        result = func(*args, **kwargs)        # Call the actual function
        end_time = time.time()                # Record end time
        duration = end_time - start_time
        print(f"⏱️ {func.__name__} took {duration:.4f} seconds to execute")
        return result
    return wrapper

# 🔽 Sample function to test timing
@timer_decorator
def slow_function():
    print("Starting slow function...")
    time.sleep(2)
    print("Finished!")

# 🚀 Call the function
if __name__ == "__main__":
    slow_function()
