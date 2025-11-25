pb_global_b = 12 # global variable
def my_function():
    print(pb_global_b) # Accessing the global variable inside the function

my_function()  # Output: 12

# Trying to access the local variable outside the function will result in an error
print(pb_global_b)  # Output: 12

def my_function():
    pb_a =10  # local variable
    print(pb_a) # Accessing the local variable inside the function
    print(pb_global_b) # Accessing the global variable inside the function

my_function()  # Output: 12

print(pb_global_b)  # Output: 12
print(pb_a)  # This will raise an error because pb_a is not defined outside the function
# here pb_a is local variable and pb_globla_b is global variable
# scope of pb_a is limited to my_function only
# trying to access pb_a outside the function will result in an error
