# ques : create a function which will take 3 values from user and which are length of a triangle. Side1, side2 , side 3
# if side1 == side2 == side3 : print isosceles triangle
def triangle_type(side1, side2, side3):
    """This function takes the lengths of the three sides of a triangle and returns its type."""
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return "Please enter positive lengths for all sides."
    if side1 == side2 == side3:
        return "Equilateral triangle"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"
# calling the function and storing the result in a variable
result = triangle_type(5, 5, 8)
print("The type of the triangle is:", result)