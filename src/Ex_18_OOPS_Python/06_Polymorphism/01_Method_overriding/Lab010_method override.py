# Polymorphism means one function name, Multiple forms/behaviors
# Types :
# Method Overriding : a child class redefines methods from Parent class
# method overloading in python is not possible directly


class Basetest:
    def run(self):
        print("running generic test")



class LoginTest(Basetest):
    def run(self):
        print("running Login test")

# this overridden

# in method override jis class ka object creation hoga uska method run hoga humesha

t = LoginTest() # since i have created object of login test then method inside login-test will run
t.run() # running Login test

t = Basetest()
t.run()

# here we have created object of base class then method running will be of Basetest class only

