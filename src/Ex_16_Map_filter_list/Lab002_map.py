name = ["alice", "bob", "charlie", "david"]

def upper_case(string):
    return string.upper()

# s = upper_case("swiss")
# print(s)

upper_name = list(map(upper_case, name))
print("Upper case names :", upper_name)
# expected output: ['ALICE', 'BOB', 'CHARLIE', 'DAVID']
# explain how map works here
# map(upper_case, name) returns a map object
# we convert the map object to list using list() function
# map returns a name one by one and applies the function upper_case to each name
# finally we get a list of names in upper case
# syntax: map(function_name, iterable) here in this case iterable is a list of names
# maps works with single parameter function here upper_case function takes single parameter string