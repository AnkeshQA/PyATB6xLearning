my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "role": "Developer"
}
print("Original Dictionary:", my_dict)

# access values using keys
print(my_dict["name"])
print(my_dict["age"])
print(my_dict["city"])
print(my_dict["role"])

# change value of existing key
my_dict["age"] = 31
print("Updated age:", my_dict["age"])

# delete a key-value pair
del my_dict["role"]
print("Dictionary after deleting role:", my_dict)

# how to iterate through a dictionary using for loop
for key,value in my_dict.items():
    print(key, value)

# check if key exists in dictionary
print("age" in my_dict)  # True
print("role" in my_dict)  # False