# A class inherits from another class, and that class itself inherits from another class.
# Grandfather passes knowledge to Father
# Father passes knowledge to Son

class Grandparent:
    def house(self):
        print("Grandparent owns a house")

class Parent(Grandparent):
    def car(self):
        print("Parent owns a car")

class Child(Parent):
    def bike(self):
        print("Child owns a bike")

c = Child()
c.house()
c.car()
c.bike()
