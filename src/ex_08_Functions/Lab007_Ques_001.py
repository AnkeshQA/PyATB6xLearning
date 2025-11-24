# function within a function
def outer_function():
    print("Outer function called")
    #step1: define inner function
    def inner_function():
        print("Inner function called")
    #step2: call inner function
    inner_function()
# calling the outer function
outer_function()