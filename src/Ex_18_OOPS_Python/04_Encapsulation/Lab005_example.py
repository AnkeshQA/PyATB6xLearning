class Bank:
    def __init__(self, balance,account_number):
        self.balance = balance # public
        self.__account_number = account_number # private

    def check_balance(self):
        print(self.balance)


    def deposit(self,amount):
        self.balance = self.balance + amount

    def show_me_account_number(self, is_auth):
        if is_auth == True:
            print(self.__account_number)
        else:
            print("Not Allowed!")
# variable (account number) is encapsulated by the method (show_me_account_number) this is called as encapsulation


icici = Bank(1000, 9876543210)
icici.deposit(100)
icici.check_balance()
# print(icici.__account_number)
# if you are cashier you can see the a/c because  of the encapsulation.
icici.show_me_account_number(True)