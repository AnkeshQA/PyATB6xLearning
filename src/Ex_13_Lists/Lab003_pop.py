my_list = [1, 2, 3, 4, 5]

# pop() : to remove element from the list based on index
popped_element = my_list.pop(2) # remove element at index 2
print("after pop element at index 2 :", my_list)
print("popped element :", popped_element)
# pop() without index removes the last element
last_element = my_list.pop()
print("after pop last element :", my_list)
print("last popped element :", last_element)

# pop() returns the removed element

#clear() : to remove all elements from the list
my_list.clear()
print("after clear my_list :", my_list)


number = [10, 20, 30, 40, 50]
print(number.index(30))

#count() : to count the occurrences of an element in the list
num_list = [1, 2, 2, 3, 4, 2, 5]
count_2 = num_list.count(2)
print("Count of 2 in num_list :", count_2)

#sort() : to sort the list in ascending order
unsorted_list = [5, 2, 9, 1, 5, 6]
unsorted_list.sort()
print("Sorted list :", unsorted_list)
#reverse() : to reverse the list
unsorted_list.reverse()
print("Reversed list :", unsorted_list)

#max() and min() : to find the maximum and minimum element in the list
max_element = max(unsorted_list)
min_element = min(unsorted_list)
print("Maximum element in unsorted_list :", max_element)
print("Minimum element in unsorted_list :", min_element)

#sum() : to find the sum of all elements in the list
sum_of_elements = sum(unsorted_list)
print("Sum of elements in unsorted_list :", sum_of_elements)

#slice() : to get a sublist from the list
slice_list = unsorted_list[1:4] # get elements from index 1 to 3
print("Sliced list from index 1 to 3 :", slice_list)

print(unsorted_list[-1])  # last element
print(unsorted_list[-2])  # second last element
print(unsorted_list[-3])  # third last element

print(20 in unsorted_list)  # check if 20 is in the list
print(100 in unsorted_list)  # check if 100 is in the list

# list creation and comprehension
l = list(range(1,5))
print("List created using range():", l)


# list of list also kown as nested
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix:", matrix)
print("Element at row 1, column 2:", matrix[1][2])

#del keyword to delete element from list
del matrix[0]  # delete first row
print("Matrix after deleting first row:", matrix)
del matrix[1][1]  # delete element at row 1, column 1
print("Matrix after deleting element at row 1, column 1:", matrix)