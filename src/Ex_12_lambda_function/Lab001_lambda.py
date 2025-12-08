def triple_number(x):
    return x * 3

result = triple_number(7)
print("The triple of the number is:", result)

# Using lambda function
triple_lambda = lambda x: x * 3
result_lambda = triple_lambda(7)
print("The triple of the number using lambda is:", result_lambda)

# Output:
# The triple of the number is: 21
# The triple of the number using lambda is: 21
#explanation:
# using lambda function to triple a number
#lambda (arguments) : expression
# here, x is the argument and x * 3 is the expression