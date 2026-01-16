key = ["name", "age", "city"] # list 1
value = ["John", 30, "New York"] # list 2
my_dict = dict(zip(key, value))
print("Dictionary created using zip():", my_dict)

# explanation:
# In this code, we create two lists: 'key' containing the keys and 'value' containing the corresponding values.
# We then use the zip() function to pair each key with its corresponding value.
# Finally, we convert the zipped object into a dictionary using the dict() function.

#merge two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
merged_dic = dict1 | dict2
print("Merged Dictionary:", merged_dict)
print("Merged Dictionary using | operator:", merged_dic)
# explanation:
# In this code, we have two dictionaries, 'dict1' and 'dict2'.
# We merge them into a new dictionary called 'merged_dict' using the unpacking operator (**).
# Alternatively, we can also use the '|' operator (available in Python 3.9 and later) to merge the dictionaries into 'merged_dic'.

# value not matching keys in two dictionaries
keys1 = ["name", "age", "city", "country"]
values1 = ["Alice", 25, "Los Angeles"]
my_dics =dict(zip(keys1, values1))
print("Value not matching keys in two dictionaries:", my_dics)