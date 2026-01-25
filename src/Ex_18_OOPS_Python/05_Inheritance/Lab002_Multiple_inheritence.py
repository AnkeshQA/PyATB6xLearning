# One parent class → Multiple child classes
# Many children inherit from the SAME parent.
# a class inherits from more than one parent class

class Father:
    def driving(self):
        print("I can drive a car")

class Mother:
    def cooking(self):
        print("I can cook food")

class Child(Father, Mother):
    def playing(self):
        print("I can play cricket")

c = Child()
c.driving()
c.cooking()
c.playing()

# Child inherits from Father
# Child inherits from Mother
# So Child gets methods of BOTH

class BrowserActions:
    def open_browser(self):
        print("Opening browser")

class LoginActions:
    def login(self):
        print("Logging into application")

class TestCase(BrowserActions, LoginActions):
    def run_test(self):
        self.open_browser()
        self.login()
        print("Executing test case")

t = TestCase()
t.run_test()


class APIBase:
    def api_auth(self):
        print("Authenticatin API")


class DBBase:
    def db_connect(self):
        print("Connecting to the DB")


class TestHybrid(APIBase, DBBase):
    def run(self):
        self.api_auth()
        self.db_connect()
        print("Test Case Running.")


tc1 = TestHybrid()
tc1.run()