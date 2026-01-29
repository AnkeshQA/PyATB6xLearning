class TestSuite:
    def info(self):
        print("this is GrandFather -- step 1")


class BaseTest(TestSuite):
    def setup(self):
        print("basetest --F -- Step2")


class UITest(BaseTest):
    def run(self):
        self.info()
        self.setup()
        print("running test case")


test = UITest()
test.run()


# o/p
# this is GrandFather -- step 1
# basetest --F -- Step2
# running test case