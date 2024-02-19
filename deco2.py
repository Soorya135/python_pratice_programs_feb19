def log_arguments(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments passed to {func.__name__}: {args}, {kwargs}")
        return func(*args, **kwargs)

    return wrapper


@log_arguments
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
