for i in range (0,10,1):
    if i == 5 or i ==6:
        print(i)  # pass is a placeholder that does nothing
    else:
        pass
        # print("no o/p")  # this line is commented out to demonstrate pass

# "expression and result table"
# # | i | expression     | result |"
# # |---|----------------|--------|
# # | 0 | i == 5 or 6   | False  | no o/p nothing will be printed
# # | 1 | i == 5 or 6   | False  | no o/p nothing will be printed
# # | 2 | i == 5 or 6   | False  | no o/p nothing will be printed
# # | 3 | i == 5 or 6   | False  | no o/p nothing will be printed
# # | 4 | i == 5 or 6   | False  | no o/p nothing will be printed
# # | 5 | i == 5 or 6   | True   | o/p = 5
# # | 6 | i == 5 or 6   | True   | o/p = 6
# # | 7 | i == 5 or 6   | False  | no o/p nothing will be printed
# # | 8 | i == 5 or 6   | False  | no o/p nothing will be printed
# # | 9 | i == 5 or 6   | False  | no o/p nothing will be printed
#  output
#  5
#  6