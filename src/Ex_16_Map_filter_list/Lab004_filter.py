# syntax : filter(function, iterable)
# filter is a function which is used to filter the items of an iterable (list, tuple etc.)
# returns a filter using a condition (return true only those items that satisfy the condition)
# filter works with single parameter function
# function should return true or false
nums = [10, 15, 22, 33, 42, 55, 60]
def is_even(x):
    return x % 2 == 0
even_nums = list(filter(is_even, nums))
print("Even numbers :", even_nums)
# expected output: [10, 22, 42, 60]
# explain how filter works here
# filter(is_even, nums) returns a filter object
# we convert the filter object to list using list() function
# filter returns a number one by one and applies the function is_even to each number
# if the function returns true for a number, that number is included in the final list
# finally we get a list of even numbers