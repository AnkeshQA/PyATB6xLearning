# list is mutable
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
my_list[2] = "PRAMOD"  # changing the third element
print("Modified list:", my_list)

# USING FOR LOOP TO ITERATE THROUGH LIST
for item in my_list:
    print("List item:", item)

# range() also returns list

for i in range(1,5):
    print("Range item:", i)