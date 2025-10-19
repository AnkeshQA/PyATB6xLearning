# WAP to calculate area of the circle
# formula area = pie * r^2 take pie and 3.14

# i/p is float
#o/p is string --> float area, print area


# logic building
# || step 1|| figure out i/p and o/p
r = float(input("enter value of radius\n"))

#||step 2||
area = 3.14* pow(r,2)

print(f"area of the circle is , {area: .2f}")

# formated string f string we use and {area} taken from step 2 and .2f will give data in 2 decimal only used in float
# this is call string data formatting or f-strings
#will learn in string class





