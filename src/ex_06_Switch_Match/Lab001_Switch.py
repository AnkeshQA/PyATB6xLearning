"""
repeat a block of code multiple times we use loops

Block of Code :
1. something to print that you want
2. some code can execute multiple times

Types of Loops:
For Loop
While loop


Conditions:
If - Else
Switch : There is no concept of switch statement
Match - case : there is no concept of break here
default is _ in this case


"""
day = int(input("enter the day \n"))
match day:
    case 1:
        print("monday")
    case 2:
        print("Tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("invalid input")

