# # - Abstraction in Python is a fundamental concept in object-oriented programming.
# # - focuses on hiding complex implementation details while exposing only the essential features of an object.
#
# To create an abstract class in Python, you need to:
#
# 1. Import the `ABC`  class and the `abstractmethod`  decorator from the `abc`  module.
# 2. Define a class that inherits from `ABC` .
# 3. Use the `@abstractmethod`  decorator to define abstract methods.

# Abstraction
# Hide the details and show what is required.

# Car - with key _ __private, tyres -> public,

# Car -> multiple - Engine, GearBox
# Car -> driver -> Engine, gearbox?

from abc import ABC, abstractmethod

#abc = abstract base class

#rules for abstraction

# 1. you have to use ABC as inheritance to mark a class as abstract
# 2. you have to use @abstractmethod annotations for methods which are abstract in nature
class Animal(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self): #
#  @abstractmethod
#     def sound(self):
#         pass
# this is completed in child class

        print("Bark")

dog = Dog("PP")
# When you write Dog("PP"), you are indirectly calling the Animal class constructor,
# and passing "PP" as the value for its name parameter.
# generally we don't have body for abstract method
dog.sound()