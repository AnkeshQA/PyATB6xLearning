"factorial program is product of all postive number "

"edge case  = 100000000 large integer,user enter string,blank,symbol,special,float"

number = int(input("Enter a number: "))
fact = 1
if number < 0:
    print("Fact is not defined")
if number == 0:
    print("FACT =", fact)
else:
    for i in range(1,number+1):
        fact = fact * i


print("FACTRORIAL OF :", fact)


"expression and result table"
# | i | expression | result |"
# |---|------------|--------|
# | 1 | i <= number | True  | fact = 1 * 1 = 1
# | 2 | i <= number | True  | fact = 1 * 2 = 2
# | 3 | i <= number | True  | fact = 2 * 3 = 6
# | 4 | i <= number | True  | fact = 6 * 4 = 24
# | 5 | i <= number | True  | fact = 24 * 5 = 120
# | 6 | i <= number | False | loop ends
# output
# Enter a number: 5
# FACTRORIAL OF : 120