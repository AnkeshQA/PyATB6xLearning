class TestSuite:
    def info(self):
        print("Test suite info called")


class BaseTest(TestSuite):
    def setup(self):
        print("Base test setup called")


    def run(self):
        print("Base test run done")


class Login(BaseTest):
    def run(self): # overriding
        print("Login called")


class APItest(BaseTest):
    def run(self): # overriding again
        print("API test called")


t = Login()
t.run()

t1 = APItest()
t1.run()