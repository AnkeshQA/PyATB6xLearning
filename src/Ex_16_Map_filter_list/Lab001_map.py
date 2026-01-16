# map (function , iterable)
# a function which is applied to each and every item of iterable (list, tuple etc.)
# returns a map object (which is an iterator)

number = [1, 2, 3, 4, 5]
def sq(x):
    return x ** 2

sq_all_number = list(map(sq, number))
# map(sq, number) returns a map object
# we convert the map object to list using list() function
# map returns a number one by one and applies the function sq to each number
# finally we get a list of squared numbers
print("map object :", sq_all_number)
print("type of map object :", type(sq_all_number))