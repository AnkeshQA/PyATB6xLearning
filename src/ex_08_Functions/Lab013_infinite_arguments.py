def print_mul_args(*args):
    """This function takes an arbitrary number of arguments and prints each one."""
# args - list
# args --> argument1, argument2, argument3, ....its argument name can take multiple values
    for i in args:
        print(i)

# calling the function with multiple arguments
print_mul_args("apple", "banana", "cherry")
print_mul_args(1, 2, 3, 4, 5)
print_mul_args("Python", 3.8, True, None)