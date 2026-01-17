# remove duplicate values from dictionary
# input_dict = {
#     'a': 100,
#     'b': 200,
#     'c': 100,
#     'd': 300,
#     'e': 200
# }
# o/p : {'a': 100, 'b': 200, 'd': 300}

input_dict = {
    'a': 100,
    'b': 200,
    'c': 100,
    'd': 300,
    'e': 200
}
unique_value= set()
results = {}
for key, value in input_dict.items():
    if value not in unique_value:
        results[key] = value
        unique_value.add(value)

print("Dictionary after removing duplicate values :", results)

#explanation:
# In this code, we initialize an empty set called 'unique_value' to keep track of unique values.
# We also initialize an empty dictionary called 'results' to store the final result.
# We iterate through each key-value pair in the input dictionary using the items() method.
# For each pair, we check if the value is already in the 'unique_value' set.
# If the value is not in the set, we add it to the set and also add the key-value pair to the 'results' dictionary.
# Finally, we print the 'results' dictionary, which contains only unique values.
# result will contain value as { a :1} next time you run it b will get stored {b:2}
