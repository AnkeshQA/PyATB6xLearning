print("outside the class")

class MobilePhone:
    model = None

    def __init__(self):
        print("default constructor")

    def talk(self):
        print("Mobile Phone talk")

iphone = MobilePhone() # object reference
iphone.talk() # calling of the function

print("outside the class2")

#  when we write this iphone = MobilePhone() then, def __init__(self): is automatically called