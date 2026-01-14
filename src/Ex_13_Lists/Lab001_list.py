# what is List, tuple and dictionary ?
# list is an ordered collection of items which is mutable (changeable) and allows duplicate elements
# it allows us to store elements of different data types in one container

# list example
my_list =[1,2,3] # same data type elements
my_list2 = [1, "hello", 3.5, True] # different data type elements
print("my_list :", my_list)
print("my_list2 :", my_list2)
print(type(my_list))
print(type(my_list2))
print(len(my_list2)) # length of list

# these are index based collections
print(my_list2[0]) # first element
print(my_list2[1]) # second element
print(my_list2[6]) # index error : list index out of range


#create empty list
empty_list = []
print("empty_list :", empty_list)
print("type of empty_list :", type(empty_list))