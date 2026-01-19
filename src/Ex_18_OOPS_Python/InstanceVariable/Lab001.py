# instance variable

a = 10 # variable available everywhere

class Person:
    b = 11 # instance variable. this is available inside the class
    def print(self):
        c = 20 # local variable exist inside the method only
        print(c)
        print(self.b)
        print(a)

object_Ref = Person()
# not allowed
# print(b)
# print(c)
