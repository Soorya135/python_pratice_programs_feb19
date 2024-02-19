# Define a decorator function that accepts arguments
def my_decorator_with_args(arg1, arg2):
    def decorator(func):
        def wrapper():
            print(f"Decorator arguments: {arg1}, {arg2}")
            print("Something is happening before the function is called.")
            func()  # Call the original function
            print("Something is happening after the function is called.")
        return wrapper
    return decorator

# Define a function and apply the decorator with arguments to it
@my_decorator_with_args("arg1_value", "arg2_value")
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()
