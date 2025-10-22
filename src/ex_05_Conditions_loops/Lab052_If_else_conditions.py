"""
problem to find max between two numbers

# logic building
Step1
i/p user inputs int or float
o/p print which ever is greater return it
handling edge cases
num1 == num2
num should be greater than 0 depends on user ask always ask interviewer
if num1 > 0 and num2 > 0:
    print("number is positive")
"""
num1 = float(input("enter the number1 \n"))
num2 = float(input("enter the number2\n"))
if num1 > 0 and num2 > 0:
    print("number is positive")
    if num1 >= num2:
        print("maximum", num1)
    else:
      print("maximum", num2)