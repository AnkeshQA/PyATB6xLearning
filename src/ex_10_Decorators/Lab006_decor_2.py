def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1: Before function call")
        func()
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2: after function call")
        func()
    return wrapper

@decorator1
@decorator2
def my_function():
    print("Inside my_function")
my_function()    