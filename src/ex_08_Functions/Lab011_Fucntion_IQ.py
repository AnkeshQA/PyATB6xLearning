# create a program to sum three numbers from user input
# if user doesn't enter any number , use de value 100,200,300 respectively


# logic building formula
#step 1 i/o and o/p analysis
# step 2 rough logic building
#return n1+n2+n3
# write the logic

num1 = int(input("Enter first number \n"))
num2 = int(input("Enter second number \n"))
num3 = int(input("Enter third number \n"))
def sum_three_numbers(n1=100, n2=200, n3=300):
    """This function takes three numbers as input and returns their sum."""
    return n1 + n2 + n3
# calling the function and storing the result in a variable
result = sum_three_numbers(num1, num2, num3)
#print("The sum of the three numbers is:", result)
# calling the function without user input to use default values
default_result = sum_three_numbers()
#print("The sum of the three default numbers is:", default_result)

result = sum_three_numbers(n1=500)
print("The sum of the 1 numbers is:", result)
result1 = sum_three_numbers(n1=100, n2=100)
print("The sum of the 2 numbers is:", result1)
result2 = sum_three_numbers(n1=10, n3=100)
print("The sum of the 2 numbers is:", result2)


# the argument name you have used should never be same as argument you are passing (which user using as user input)