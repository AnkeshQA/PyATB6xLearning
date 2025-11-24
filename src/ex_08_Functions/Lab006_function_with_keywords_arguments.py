# function with keyword arguments
def display_info(name, role):
    print(f"Name: {name}, Role: {role}")
    print(f"Name: {name}, Role: {role}")
# calling the function with keyword arguments
display_info(role="Admin", name="Shrikant")
display_info(name="Ankesh", role="User")

# In this example, we define a function display_info that takes two parameters: name and role.
# When calling the function, we use keyword arguments to specify the values for each parameter.
# This allows us to pass the arguments in any order, making the function calls more readable and flexible.
# Output:
# Name: Shrikant, Role: Admin
# Name: Ankesh, Role: User
