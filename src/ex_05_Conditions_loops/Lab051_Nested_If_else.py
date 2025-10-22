"""
find the positive number which is even or odd
"""

num = int(input("enter the number\n").strip())
if num >= 0:

    if num %2 == 0:
        print("even")
    else:
        print("odd")
else:
    print("negative number")

# can be used via ternary operator
"""
one line code is never optimised code 
reducing number of variable is optimised code 
"""
if num >= 0:
    print("even" if num % 2 ==0 else "odd")
else:
    print("negative number")