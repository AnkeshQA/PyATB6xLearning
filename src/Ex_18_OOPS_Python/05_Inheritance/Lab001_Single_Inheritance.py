# inheritance lets a class (child/subclass) reuse attributes and methods of another class
# it promotes code reuse and organization and models real worlds relationships


#types
# Single inheritance ---> one parent and one child

# a subclass/child class inherits from one Parent/Base class


class Base_test:
    driver = "chrome" #public
    __driver2 = "Firefox" #private
    def setup(self):
        print("base setup with browser and env")
        print("running test   " + self.__driver2)

class login_test(Base_test):
    def run(self):
        self.setup()
        print("running test   " + self.driver )
        # print("running test   " + self.__driver2)
        # AttributeError: object has no attribute '__driver2'
        #Child class is not allowed to touch it directly.
        print(self._Base_test__driver2)
        # When you write: __driver2
        # Python secretly renames it to: _Base_test__driver2
        # NOT recommended in real projects.
        #This is called Name Mangling


t = login_test()
t.run()
