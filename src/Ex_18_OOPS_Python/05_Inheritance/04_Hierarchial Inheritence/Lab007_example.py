class Basetest:

    def setup(self):
        print("setup from basetest")

class Login(Basetest):
    def run(self):
        print("running login test")

class SignUp(Basetest):
    def run(self):
        print("running signup test")


Login().setup()
Login().run()

SignUp().setup()
SignUp().run()