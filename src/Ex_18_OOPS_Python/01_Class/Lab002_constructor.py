# constructor is special type of function
# called automatically when you create an object
# it will be a method because it's within the class
# types : default constructor (no arguments)
# Parameterised constructor (with argument)
# constructor doesn't return anything
#__init__name of the constructor
# self --> current object , __init__ --> constructor

class Dog:
#attribute
    name = None
    breed = None
    height = None
    weight = None
#behaviour
    def bark(self):

        print("barking")
        print(self.name) #using this we can access the attributes of the class


# when method is created in a class , the first argument will be always self
# by using self we can access all the variables which is name , breed, height etc basically (attributes)
# directly attributes cannot be accessed in a method
    # print(name)

print("outside the class")

#create an object of a class
chow = Dog()
#h here dog() is object
# chow --> object reference. It cann access the methods & it can access the attributes also
rancho = Dog()