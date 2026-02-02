# try:
#     # code that may throw error
# except:
#     # handle the error
# else:
#     # runs only if no exception
# finally:
#     # always runs

# What is the difference between error and exception?
# - Errors = serious issues (memory, syntax)
# - Exceptions = runtime issues you can handle (Error in the end)
a = int(input("Enter num 1"))
b = int(input("Enter num 2"))
try:
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Error becoz of the zero div b !=0")