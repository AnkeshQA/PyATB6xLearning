"FizzBuzz Test"
"Write a program that prints numbers from 1 to 100."
"However, for multiples of 3, print Fizz instead of the number, and for multiples of 5, print Buzz For numbers that are multiples of both 3 and 5, print FizzBuzz."
# print numbers from 1 to 100 with FizzBuzz rules
# for multiple of 3 print Fizz
# for multiple of 5 print Buzz
# for multiple of both 3 and 5 print FizzBuzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
# Output will be:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# ...
# 98
# Fizz
# Buzz
