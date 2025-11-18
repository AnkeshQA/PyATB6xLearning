# continue it skips the current iteration and goes to the next iteration of the loop
for number in range (10):
    if number %2 ==0:
        continue
    else:
        print(number)
# "expression and result table"
# # | number | expression      | result |"
# # |--------|------------------|--------|
# # | 0      | number % 2 == 0  | True   | no o/p (skipped)
# # | 1      | number % 2 == 0  | False  | o/p = 1
# # | 2      | number % 2 == 0  | True   | no o/p (skipped)
# # | 3      | number % 2 == 0  | False  | o/p = 3
# # | 4      | number % 2 == 0  | True   | no o/p (skipped)
# # | 5      | number % 2 == 0  | False  | o/p = 5
# # | 6      | number % 2 == 0  | True   | no o/p (skipped)
# # | 7      | number % 2 == 0  | False  | o/p = 7
# # | 8      | number % 2 == 0  | True   | no o/p (skipped)
# # | 9      | number % 2 == 0  | False  | o/p = 9
# # output
# # 1
# # 3
# # 5
# # 7
# # 9