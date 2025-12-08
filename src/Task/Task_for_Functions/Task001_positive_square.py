# ques: create a function which will take a positive number from user and return the square of that number
def square_of_number(number):
    """This function takes a positive number as input and returns its square."""
    if number < 0:
        return "Please enter a positive number."
    return number * number
# calling the function and storing the result in a variable
result = square_of_number(6)
print("The square of the number is:", result)