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

# union() : to combine two sets
set1 = {1,2,3}
set2 = {3,4,5}
set3 = set1.union(set2)
set3 = set1 | set2  # alternative way to do union
print("set3 after union of set1 and set2 :", set3)
# intersection() : to get common elements between two sets
set4 = set1.intersection(set2)
set4 = set1 & set2  # alternative way to do intersection
print("set4 after intersection of set1 and set2 :", set4)
# difference() : to get elements in set1 but not in set2
set5 = set1.difference(set2)
print("set5 after difference of set1 and set2 :", set5)
set5 = set1 - set2  # alternative way to do difference
print("set5 after difference of set1 and set2 :", set5)
# symmetric_difference() : to get elements in either set1 or set2 but not in both
set6 = set1.symmetric_difference(set2)
set6 = set1 ^ set2  # alternative way to do symmetric difference
print("set6 after symmetric difference of set1 and set2 :", set6)
# add() : to add element to the set
set1.add(6)
print("set1 after add 6 :", set1)