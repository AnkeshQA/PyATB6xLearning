# write a program to calculate even and odd numbers using lambda function and user input.
# Getting user input
number = int(input("Enter a number: "))
# Lambda function to check even or odd
even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
# Calling the lambda function and storing the result
result = even_odd(number)
print(f"The number {number} is {result}.")
# Explanation:
# We define a lambda function 'even_odd' that takes one argument 'x'.
# The function checks if 'x' is divisible by 2 (using the modulus operator %).
# If it is, the function returns "Even"; otherwise, it returns "Odd".
# We then call this lambda function with the user-provided number and print the result.
# Output:
# Enter a number: 5
# The number 5 is Odd.
# Enter a number: 8
# The number 8 is Even.