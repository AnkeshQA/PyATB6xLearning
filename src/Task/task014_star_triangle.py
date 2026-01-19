#*
#* *
#* * *
#* * * *
#* * * * *
# def print_star_triangle(n):
#     for i in range(1, n + 1):
#         print('* ' * i)
# # Example usage
# print_star_triangle(5)


row = int(input("enter the value for the right angle triangle"))

for i in range(1, row + 1):
    for j in range(i):
        print('* ', end="")
    print()
