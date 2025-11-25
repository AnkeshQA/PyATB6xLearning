# user defined functions
# 1. they cant return --> non returning function
# 2. they can return --> returning function
# 3. they can have parameters/ arguments
# 4. they dont have parameters/ arguments
import math

# built-in function example
result = max(3,4)
print(result)

#1. No return type and no parameters/ arguments
def greet():
    print("Hello User! Welcome to Python Functions")

greet()

#2. No return type but with parameters/ arguments
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python Functions")
greet_user("Shrikant")


# 3. With no return type and with parameters/ arguments
def say_hello_default_arg(name ="Ankesh"):
    print("hello",name.upper())

say_hello_default_arg()
say_hello_default_arg("Shrikant")

# passing multiple parameters/ arguments
def multiple_args(name1 = "A", name2= "B"):
    print("mul ->", name1 , name2)
multiple_args()
multiple_args("Shrikant", "Ankesh")
multiple_args(name1="Shrikant")
multiple_args(name2="Ankesh")
multiple_args(name2="Ankesh", name1="Shrikant")


# 4. With return type and with parameters/ arguments
def add_numbers(num1=100, num2 =200):
    return num1 + num2

result = add_numbers()
print("Addition Result:", result)
result = add_numbers(10, 20)
print("Addition Result:", result)
result = add_numbers(num2=50)
print("Addition Result:", result)
result = add_numbers(num1=30, num2=70)
print("Addition Result:", result)