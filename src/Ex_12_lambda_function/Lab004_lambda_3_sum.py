def sum_three_numbers(a, b, c):
    """
    This lambda function takes three numbers as input and returns their sum.
    """
    return a+b+c
# calling the lambda function and storing the result in a variable
sum_l = lambda a, b, c : a + b + c
result = sum_l(5, 10, 15)
print("The sum of three numbers using lambda is:", result)
# explanation
# using lambda function to sum three numbers
# lambda (arguments) : expression
# here, a, b and c are the arguments and a + b + c is the expression
# Output:
# The sum of three numbers using lambda is: 30