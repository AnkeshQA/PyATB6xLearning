#example 2 : lets create a function which will greet you or say hello to user
def greet_user(name):
    print("Hello User! Welcome to Python Functions" , name)

# step 2 : call the function
greet_user("Shrikant")
greet_user("Ankesh")

def greet_user_fullname(first_name, last_name):
    print("Hello User! Welcome to Python Functions" , first_name + " " + last_name)

# step 2 : call the function
greet_user_fullname("Shrikant", "Kumar")
greet_user_fullname("Ankesh", "Singh")

#function name should be lower case , if multiple words use underscore to separate them
#parameters are variables that are passed to function to provide input data
#arguments are the actual values passed to function during function call
#you can have multiple parameters in a function separated by comma
#while calling the function you need to pass the same number of arguments as the number of parameters defined in the function
# if you pass less or more arguments than defined parameters you will get TypeError
#example : greet_user() # TypeError: missing 1 required positional argument: 'name'
#example : greet_user("Shrikant", "Kumar") # TypeError: greet_user() takes 1 positional argument but 2 were given
#you can also use default parameters in function definition
def greet_user_default(name="User"):
    print("Hello User! Welcome to Python Functions" , name)
# step 2 : call the function
greet_user_default()
greet_user_default("Shrikant")
greet_user_default("Ankesh")