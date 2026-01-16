square = {x **2 for x in range(5)}
print("Set of squares from 0 to 4 :", square)

# one liner code to create a set of even numbers from 0 to 5
squares = set()
for x in range(5):
    squares.add(x **2)
print("Set of squares from 0 to 4 using for loop :", squares)


# frozenset : immutable set value which cannot be changed once created
# list is converted to frozenset
frozen_set = frozenset([1,2,3,4,5])
print("frozenset :", frozen_set)
print("type of frozenset :", type(frozen_set))