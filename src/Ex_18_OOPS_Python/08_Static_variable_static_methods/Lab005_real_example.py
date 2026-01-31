class ExcelReader:

    @staticmethod
    def readExcelFile():
        print("Reading from Excel")
class MYSQLDBConnection:

    @staticmethod
    def readMySQLFile():
        print("Reading from MySQL")

class TC1:

    def runTC(self):
        ExcelReader.readExcelFile()
        MYSQLDBConnection.readMySQLFile()
        print("Hi")

class TC2:

    def runTC(self):
        ExcelReader.readExcelFile()
        MYSQLDBConnection.readMySQLFile()
        print("Hello")

tc1 = TC1()
tc2 = TC2()
tc1.runTC()
tc2.runTC()

# we don't need to create multiple objects for accessing the static methods
# we can access static methods using class name directly