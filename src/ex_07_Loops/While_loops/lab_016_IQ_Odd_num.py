for i in range(101): # 0 to 100
    if i % 2 != 0:
        print(i)

# "expression and result table"
# # | i   | expression    | result |"
# # |-----|----------------|--------|
# # | 0   | i % 2 != 0    | False  | no o/p
# # | 1   | i % 2 != 0    | True   | o/p = 1
# # | 2   | i % 2 != 0    | False  | no o/p
# # | 3   | i % 2 != 0    | True   | o/p = 3
# # | 4   | i % 2 != 0    | False  | no o/p
# # | ... | ...            | ...    | ...
# # | 98  | i % 2 != 0    | False  | no o/p
# # | 99    | i % 2 != 0    | True   | o/p = 99
# # output
# # 1
# # 3
# # 5
# # 7
# # 9
# # ...
# # 97
# # 99

# Note: This code prints all odd numbers from 0 to 100.