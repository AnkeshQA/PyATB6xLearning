"""
loops is block of code that something to print that you repeat
some code you can execute multiple time
Types:
for loop
while loop

used to iterate over a sequence like a list,tuple,dictionary,string and range
What is range()?
range is a built-in python function used to generate a sequence of numbers
commonly used in for loops

Syntax :
range(start,stop, step)

range - range(start, stop-1,step)
step should be integer
range stop is always n-1 ex: 10-1
"""
# print hello world 10 times
for i in range(1,10,1):
    print("hello world")# 9 times it will print
    print(i)