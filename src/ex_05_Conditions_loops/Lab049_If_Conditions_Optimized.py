# Conditional Statements (Decision Making)
# used when we want to execute certain parts of code only If a specific condition is true

"""
if condition :
 # block of code
elif another_condition
 # block of code
else:
 # block of code
"""

"""
write a program to take a user and let him know if he can go pub 
here age limit 21

"""

"""
step 1 
i/p ==> age, int
o/p ==> string result >> can go to pub or not

Step 2
if > 21 print can go 
else < 21 print can go 

Step 3 
Write logic

Step 4 
check for edge cases.
Edge case :
1. negative ages or extremely high value inputs 
2. Non numeric inputs 
3. Age which is not valid 
step 5 
handle all edge cases 
"""

age = int(input("enter user age\n").strip())
# Strip Return a copy of the string with leading and trailing whitespace removed.

if age <= 0 or age > 130:
    print("enter the valid age")
else:
    if  age >= 21 :
        print("yes, can go to pub")
    else:
        print("no, can't go to pub")
# will discuss try catch later




