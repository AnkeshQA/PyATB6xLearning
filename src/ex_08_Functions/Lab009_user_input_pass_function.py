# task : write a program , take a user name and say hello to him/her
user_input = input("Please enter your name: \n")
# decaring the function
def say_your_name(name):
    """This function takes a name as input and greets the user."""
    print(f"Hello, {name}! Welcome to the Python Functions tutorial.")
# calling the function with user input
say_your_name(user_input)