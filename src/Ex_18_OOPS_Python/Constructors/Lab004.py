class Person:
    name = None
    age = None
    phone = None
    occupation = None

    def __init__(self):
        print("let's take a user input, Please share the name,age and phone number,occupation")
        self.name = input("Enter your name: \n")
        self.age = input("Enter your age: \n")
        self.phone = input("Enter your phone number: \n")
        self.occupation = input("Enter your occupation: \n")

    def display_values(self):
        print("name is ", self.name)
        print("age is ", self.age)
        print("phone number is ", self.phone)
        print("occupation is ", self.occupation)

#any attribute which belong to class is initialized using self.{attributeName}

amit = Person()
amit.display_values()