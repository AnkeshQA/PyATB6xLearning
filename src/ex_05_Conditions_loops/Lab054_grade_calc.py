"""
grade calculator the calculate and displays the letter grade
for a given numerical score (A,B,C,D or F)
based ona following grading scale
A: 90-100
B : 80-89
C: 70-79
D: 60-69
F: 0-59

# logic building formula
i/p user input --> score --> int
o/p --> Str --> A,B,C,D,F

"""
score = int(input("enter score : \n").strip())
if score > 100 or score <=-1:
    print("you are superman, you cannot have this grade")
else:
    if score >= 90 and score <=100:
     print("your grade is A")
    elif score >= 80 and score <=89:
        print("your grade is B")
    elif score >=70 and score <=79:
        print("your grade is C")
    elif score >=60 and score <=69:
        print("your grade is D")
    else:
        print("your grade is F")

# float and abc can be handled by try catch