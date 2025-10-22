"""
find the maximum number between 3 numbers

logic
user inputs -- num1 , num2 , num3 --> int
o/p --> int or string with max number
"""
num1 = int(input("enter num1\n"))
num2 = int(input("enter num2\n"))
num3 = int(input("enter num3\n"))

"""
5 > 3 and 5 > 2 --> 
num1 > num2 and num1 > num3 --> num1 is max
num2 > num1 and num2> num3 --> num2 is max 
num 3 --> max 
"""
if num1 > num2 and num1 > num3:
    print("max",num1)
elif num2 > num1 and num2> num3:
    print("max",num2)
else:
    print("max",num3)

"""
when you more than 2 conditions use elif 
when you have only two conditions use if-else
"""




"""
num1 = 5, num2 = 5 and num3 = 2
"""
if num1 >= num2 and num1 >= num3:
    print("max",num1)
elif num2 > num1 and num2> num3:
    print("max",num2)
else:
    print("max",num3)