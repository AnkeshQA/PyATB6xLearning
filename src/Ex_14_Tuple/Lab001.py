# tuple - immutable (unchangeable) ordered collection of items which allows duplicate elements
# tuple example
my_tuple = (1,2,3) # same data type elements
my_tuple2 = (1, "hello", 3.5, True) # different data type elements
print("my_tuple :", my_tuple)
print("my_tuple2 :", my_tuple2)
print(type(my_tuple))
print(type(my_tuple2))
print(len(my_tuple2)) # length of tuple
# these are index based collections
print(my_tuple2[0]) # first element
print(my_tuple2[1]) # second element
# print(my_tuple2[6]) # index error : tuple index out of range
# tuples are immutable
# my_tuple2[1] = "Ankesh" # TypeError: 'tuple' object does not support item assignment
# print("after changing index 1 to 'Ankesh' :", my_tuple2)
# tuple methods
# count() : to count the occurrences of an element in the tuple
count_hello = my_tuple2.count("hello")
print("Count of 'hello' in my_tuple2 :", count_hello)
# index() : to find the index of an element in the tuple
index_3_5 = my_tuple2.index(3.5)
print("Index of 3.5 in my_tuple2 :", index_3_5)
# tuples are generally used when we want to ensure that the data remains constant and unchanged throughout the program
# they are also used to store data that should not be modified, such as coordinates, RGB values, etc.
# tuples can be used as keys in dictionaries because they are immutable, whereas lists cannot be used as keys

# tuple with single element
single_element_tuple = (5,)
print("single_element_tuple :", single_element_tuple)
print("type of single_element_tuple :", type(single_element_tuple))
