# list is mutable
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
my_list[2] = "Ankesh"  # changing the third element
print("Modified list:", my_list)

# USING FOR LOOP TO ITERATE THROUGH LIST
for item in my_list:
    print("List item:", item)

# range() also returns list

for i in range(1,5):
    print("Range item:", i)

# range is a function which creates a list and returns the list


my_list = [1,2,3,4,5]
print("elements at the index 0 - " , my_list[0])
print("elements at the index 1 - " , my_list[1])
print("elements at the index 2 - " , my_list[2])
print("elements at the index 3 - " , my_list[3])
print("elements at the index 4 - " , my_list[4])
#print("elements at the index 5 - " , my_list[5]) # index error : list index out of range

# elements are stored into indexation
# index starts from 0 to n-1 (n is length of list)
# append() : to add element at the end of the list
# when you append anything it doesn't return anything it just modifies the original list
my_list.append(4)
print("after append 4 :", my_list)
my_list.append("hello")
print("after append 'hello' :", my_list)


# extend() : to add multiple elements at the end of the list
my_list.extend([7,8,9,10])
print("after extend [7,8,9,10] :", my_list)

# insert() : to add element at specific index
my_list.insert(2, "Ankesh") # insert 'Ankesh' at index 2
print("after insert 'Ankesh' at index 2 :", my_list)

my_list[1] ="amit"  # changing element at index 1
print("after changing index 1 to 'Ankesh' :", my_list)

# remove() : to remove element from the list
my_list.remove("Ankesh") # remove 'Ankesh' from the list
print("after remove 'Ankesh' :", my_list)

#copy() : to copy the list
new_list = my_list.copy()
print("new_list after copy :", new_list)

new_list.remove("amit") # remove 'amit' from the new_list
print("new_list after remove 'amit' :", new_list)
print("original my_list remains unchanged :", my_list)

