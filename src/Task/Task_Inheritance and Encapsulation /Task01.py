"""
Build a Test Framework with Encapsulation + Inheritance
🎯 Goal:
Create a simple automation structure that uses:
A BaseTest class for setup/teardown (Parent class)
A LoginTest class that inherits BaseTest (Child class)
Encapsulate sensitive data (like credentials) as private variables
✅ Requirements:
Create a BaseTest class:
Has a protected variable _driver = "Chrome".
Method setup() prints "Launching browser: Chrome".
Method teardown() prints "Closing browser".
Create a LoginTest class that inherits BaseTest:
Has private variables for username and password.
Method run_test() that prints:
"Running login test with user: <username>".
Use encapsulation: access private vars only through a method (e.g., get_user()).
Create an object of LoginTest and call:
setup()
run_test()
teardown()
⭐O/P⭐
Launching browser: Chrome
Running login test with user: admin
Closing browser
"""




# BaseTest is the parent class
# It is responsible for common setup and teardown actions
# that can be reused by all test classes
class BaseTest:
    # Protected variable
    # Single underscore (_) means it can be accessed inside this class
    # and also inside child classes
    _driver = "Chrome"   # protected variable

    # setup() method is used to start the browser
    def setup(self):
        print("Launching browser:", self._driver)

    # teardown() method is used to close the browser
    def teardown(self):
        print("Closing browser")

# LoginTest is the child class
# It inherits BaseTest, so it can use setup() and teardown()
class LoginTest(BaseTest):
    # Private variables
    # Double underscore (__) makes these variables private
    # They cannot be accessed directly outside this class
    __username = "admin"     # private variable
    __password = "pass123"   # private variable

    def get_user(self):
        # Getter method
        # This method is used to access the private variable safely
        # This is called encapsulation
        return self.__username

    # This method runs the login test
    # It uses the getter method instead of directly accessing
    # the private variable
    def run_test(self):
        print("Running login test with user:", self.get_user())



# Creating object of LoginTest class
obj = LoginTest()

# Calling setup() method from BaseTest
obj.setup()

# Running the login test from LoginTest
obj.run_test()

# Calling teardown() method from BaseTest
obj.teardown()
