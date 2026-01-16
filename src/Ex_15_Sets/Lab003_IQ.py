# find the first non-repeating character in a given string. Using sets
# swiss -> S --> X , W--> answer


s = set()
def first_non_repeating_character(string):
    for char in string:
        if string.count(char) == 1:
            s.add(char)
            return char
    return None


print(first_non_repeating_character("swiss"))
print(s)

# Taking input from user
# input_string = input("Enter a string: ")
#
# result = first_non_repeating_character(input_string)
#
# if result:
#     print(f"The first non-repeating character in '{input_string}' is: '{result}'")
# else:
#     print(f"There are no non-repeating characters in '{input_string}'")

# syntax to create a set
# set1 = set(["the", "quick", "brown", "fox"])
# print(set1)
# print(len(set1))
# for i in set1:
#      print(i)
# set1.add("jumps")
# print(set1)