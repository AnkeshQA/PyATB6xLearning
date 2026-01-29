# One parent class → Multiple child classes

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

d = Dog()
d.eat()
d.bark()

c = Cat()
c.eat()
c.meow()

# explain
# Animal = Parent
# Dog and Cat both inherit from Animal
# So both get eat() method