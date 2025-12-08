# print
#*

#**

#***

#****

#*****


num = int(input("Enter the number of rows for the right triangle: "))
for i in range(1, num + 1):
    for j in range(i):
        print("*", end="")
    print()