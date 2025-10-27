"""
given a number you need to calculate factorial of a number
n = 5
fact = 5*2*3*4*2*1
factorial of zero is 1
"""

n = int(input("Enter a number: "))

fact = 1

# factorial of 0 and 1 is 1
if n == 0 or n == 1:
    fact = 1
else:
    for i in range(1, n + 1):
        fact *= i

print("Factorial =", fact)
