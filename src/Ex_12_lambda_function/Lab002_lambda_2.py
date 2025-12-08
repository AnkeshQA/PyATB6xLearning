def add(n):
    return n+10

add_lambda = lambda n: n + 10
result = add_lambda(5)
print("The result of adding 10 using lambda is:", result)

# explanation
# using lambda function to add 10 to a number
# lambda (arguments) : expression
# here, n is the argument and n + 10 is the expression
# Output:
# The result of adding 10 using lambda is: 15