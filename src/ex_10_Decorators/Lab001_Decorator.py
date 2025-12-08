"Decorators in Python are a powerful and flexible tool that allows you to modify the behavior of functions or methods without changing their actual code"
"They are essentially functions that take another function as an argument and extend or alter its behavior."

#primary use case :
#1. Before
#2. After
#3. Logging - add logs to the automation

#Benefits of Using Decorators
#1. Code Reusability: Decorators allow you to reuse the same functionality across multiple functions without duplicating code.
#2. Separation of Concerns: They help in separating the core logic of functions from auxiliary concerns like logging, access control, etc.
#3. Enhanced Readability: Using decorators can make your code more readable and maintainable by clearly separating different aspects of functionality.

#example
def add_security(func):
    def wrapper():
        print("1. before the function is called")
        print("2. Add helmate , dashcam, gloves , knee pads")
        func()
        print("3. after the function is called")
        print("4. Drive secure, leave all the items")
    return wrapper()


@add_security
def drive_ola_scooter():
    print("Driving Ola Scooter")


#explnation:
#1. def add_security(func):
# You are creating a decorator function.
#It accepts another function as input.
# Here, func = the function you want to protect
#    def wrapper():
#You create a new function inside it.
#This function will:
#run before
#run the original function
#run after
#This is like a gift wrapper around a gift 🎁
# ✅ Line 3
#         print("1. before the function is called")
# This runs before your main function
# ✅ Line 4
#         print("2. Add helmate , dashcam, gloves , knee pads")
# This also runs before riding
# ✅ Line 5
#         func()
# This runs your main function
# This actually calls your original function
# Without this → your original function will NEVER run
# ✅ Line 6
#         print("3. after the function is called")
# This runs after your main function finshes
# ✅ Line 7
#         print("4. Drive secure, leave all the items")
# This also runs after riding / final message after everything is done
# ✅ Line 8
#     return wrapper
# You return the wrapper function
# This means when you use @add_security, you are replacing your original function with the wrapper
# So, when you call drive_ola_scooter(), you are actually calling wrapper()












@add_security
def drive_uber_scooter():
    print("Driving Uber Scooter")