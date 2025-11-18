for i in range(0,10):
    print(i) # here print is used before break so 5 wil be printed also
    if i ==5:
        break


# break is used to terminate the loop when the condition i == 5 is met.

"expression and result table"
# | i | expression | result |"
# |---|------------|--------|
# | 0 | i == 5    | False  | o/p = 0
# | 1 | i == 5    | False  | o/p = 1
# | 2 | i == 5    | False  | o/p = 2
# | 3 | i == 5    | False  | o/p = 3
# | 4 | i == 5    | False  | o/p = 4
# | 5 | i == 5    | True   | o/p = 5 and then break the loop
# output
# 0
# 1
# 2
# 3
# 4
# 5
for i in range(0,10):
    #
    if i ==5:
        break
    print(i) # here print is used after break so 5 wil not be printed also

# break is used to terminate the loop when the condition i == 5 is met.
# o/p will be
# 0
# 1
# 2
# 3
# 4