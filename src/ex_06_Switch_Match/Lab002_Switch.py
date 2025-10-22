print("Enter the test u want to run")
test_type = input("Enter the test type : PAI, UI, Performance, Security")
match test_type:
    case "API":
        print("we are running a postman API test case ")
    case "UI":
        print("we are running selenium test case")
    case "Performance":
        print("we are running performance test case")
    case "Security":
        print("we are running security test case ")
    case _:
        print("invalid type")

# here default case will always be in the last
# if there is multiple conditions go with Match
# if there is multiple condition more than 4 conditions go for if-else

