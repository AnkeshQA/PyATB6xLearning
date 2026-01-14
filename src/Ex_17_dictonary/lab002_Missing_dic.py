# missing dictionary example
dict1 = {'a': 1, 'b': 2, 'c': 3}
print(dict1.values())
print(dict1.keys())

dict2 = {'a': 1, 'b': 2}

missing_keys = set(dict1.keys()) - set(dict2.keys())
print("Missing keys in dict2:", missing_keys)