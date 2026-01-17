# getting key and values in a dictionary

dict1 = {'name': 'John', 'age': 30, 'city': 'New York'}
print("Keys:", dict1.keys())
print("Values:", dict1.values())


dict2 = {'name': 'Joe', 'age': 30,}

#missing_keys = dict2 - dict1
#print("Keys in dict2 but not in dict1:", missing_keys)
# this will raise an error because dictionaries do not support subtraction
missing_keys = set(dict1.keys()) - set(dict2.keys())
print("Keys in dict1 but not in dict2:", missing_keys)

