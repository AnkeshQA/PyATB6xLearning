class Dog:
#attribute
    name = None
    breed = None
    height = None
    weight = None
#behavior
    #passing parameters

    def __init__(self):
    # default constructor
        print("this will be called")


    def bark(self):

        print("barking")
    def sleep(self):
        print("sleep  ")
    def talk(self):
        pass

chow_ref = Dog()
rancho_ref = Dog()

print(chow_ref.name)
print(rancho_ref.breed)

#calling of method in another way

Dog().bark()
Dog().sleep()
Dog().talk()