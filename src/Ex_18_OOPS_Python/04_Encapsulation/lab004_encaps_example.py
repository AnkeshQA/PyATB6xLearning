class Car:

    def __init__(self):
        self.public_password = "pramod" # public variable which is available everywhere
        self.__password_baby = "password123" # private variable using double underscore
    def nanny(self): #access private variable can be only done by creating a new function
        self.__password_baby = "123"
        return self.__password_baby


obj_ref = Car()
obj_ref.nanny()
print(obj_ref.public_password) # I can access variable (self.password) this is allowed
print(obj_ref.nanny()) # Private variable → access it via a method → call the method with ()

#private variable is always available within the class




