def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("before func call")
        func(*args, **kwargs)
        print("after func call")

    return wrapper


@my_decorator
def example_function(name, age):
     print(f"Hello {name}")


example_function("john", 4)