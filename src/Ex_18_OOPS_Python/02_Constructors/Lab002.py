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
#behavior
    #passing parameters

    def __init__(self,nameGiven,breedGiven): # this is now a parameterized constructor

        self.name = nameGiven
        self.breed = breedGiven


    def bark(self):

        print("barking  "  + self.name)
    def sleep(self):
        print("sleep  "  +  self.name)
    def talk(self):
        pass

chow = Dog("chow","mastiff")
rancho = Dog("rancho","mastiff")

chow.bark()
rancho.sleep()
#constructor are basically used to initialize the value of the attributes
