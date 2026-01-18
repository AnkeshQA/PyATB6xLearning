# A class is a group of objects which have common properties. A class can have some and functions(called methods)
#the class we have used is main
# it's a blueprint to create objects
# objects created from the class that is exactly real containing attributes and behavior


# class is a user defined data type which defined it is a properties and it's method
# object is a runtime entity . It's of an instance of a class
# all data members and member function of the class can be accessed with help of the objects


class Person:
    # attributes /properties / data variables
    name = None
    id = None
    email = None
    address = None
    phone = None
    age = None
    email = None
    gender = 0

# we can use Zero (0) as well here. Python is dynamic program language
    # behavior / methods
    def speak(self): # self -- this will be the first parameter of every method in class
    # this is no return type and no arguments method
        print("I can talk")

# argument with no return type method
    def sleep(selfself,name):
        print("I am a method")
        print("sleep", name)

# argument with return type method
    def sleep2(self, name):
        print("I am a method")
        return None

# non argument type and non return type method
    def walk(self):
        print("i am walking")



