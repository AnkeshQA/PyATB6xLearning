# set() = unordered , unindexed collection of unique elements, mutable (changeable), duplicates doesn't exist
# remove duplicates automatically
# set is also a list like collection but it doesn't allow duplicates
# set example
# it has curly braces {}
# my_set = {1,2,3} # same data type elements
# my_set2 = {1, "hello", 3.5, True, 2} # different data type elements
my_set = {1, 2, 3, 4,4, 5}
my_set2 = {1, "hello", 3.5, True, 2} # different data type elements
print("my_set :", my_set)
print("my_set2 :", my_set2)
print(type(my_set))
print(type(my_set2))
print(len(my_set2)) # length of set
# sets are unordered collections
# print(my_set2[0]) # TypeError: 'set' object is not sub

#tuple to set
t = (1,2,3,4,5,5)
set_from_tuple = set(t)
print("set_from_tuple :", set_from_tuple)

empty = set()
print("empty :", empty)
print("type of empty :", type(empty))


t1 = {10, 20, 30}
t1.add(40)
print("after add 10 to set t1 :", t1)

mixed_set = {1, "hello", 3.5,True}
print("mixed_set :", mixed_set)

# 1 is equal to True in set
# 0 is equal to False in set