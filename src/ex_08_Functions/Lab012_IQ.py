def sum_three_numbers(n1=100, n2=200, n3=300):
    # here n1, n2, n3 are parameters /argument with default values
    """This function takes three numbers as input and returns their sum."""
    return n1 + n2 + n3
# calling the function and storing the result in a variable
result = sum_three_numbers()
print("The sum of the three default numbers is:", result)