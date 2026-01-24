class Home:
    def __init__(self):
        self.public_var = "father" # public variable
        self._protected_var = "brother" # protected variable
        self.__private__var = "baby" # private variable

    def mom(self): #public function
        print(self.__private__var)
        self.__wife()
    # this is called encapsulation here wife is accessible by mom

    def __wife(self): #private function
        print("Private Wife")

object_ref = Home()
# object_ref.__wife()  cannot access publicly
# object_ref.__private_var

object_ref.mom()
print(object_ref._protected_var)
# ⚠️ Technically accessible, but not recommended