try:
    a = int(input("Enter num 1"))
    b = int(input("Enter num 2"))
    c = a / b
except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("Div Error")
else: # Runs only if try block succeeds.
    print(c)
finally:
    print("I will always execute!")

# explanation:
# This code snippet demonstrates the use of try, except, else, and finally blocks for exception handling in Python.
# - The try block contains code that may raise exceptions (e.g., converting input to integers and performing division).
# - The except blocks handle specific exceptions: ValueError (invalid input) and ZeroDivisionError (division by zero).
# - The else block executes only if no exceptions are raised in the try block, printing the result of the division.
# - The finally block always executes, regardless of whether an exception occurred, ensuring that cleanup or final messages are displayed.
