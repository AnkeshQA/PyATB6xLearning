def outer_function():
    var1 = 30
    def inner_function():
        var2 = 20
        # var 2 is accessible only within inner_function
        print(var1) # Accessing variable from the outer function
    def inner_function_2():
        var3 = 10
        print(var1) # Accessing variable from the outer function
        # print(var2) # This will raise an error because var2 is not defined in
        # inner_function_2
    inner_function()
    inner_function_2()
    # this is called inside outer_function
outer_function()