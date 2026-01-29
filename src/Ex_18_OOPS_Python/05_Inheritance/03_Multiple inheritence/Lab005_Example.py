class Father1:
    def money(self):
        print("Father1 owns money")


class Father2:
    def money(self):
        print("Father2 owns money")



# class Child(Father1, Father2): #using MRO father1 will be called first
class Child(Father2, Father1):
    def give_money(self):
        print("Child owns money")
        self.money()

c = Child()
c.give_money()


# MRO stands for Method Resolution Order.
#  It is the order in which Python searches for a method or attribute when
#  multiple inheritance is used. It defines which parent class method is called first
#
