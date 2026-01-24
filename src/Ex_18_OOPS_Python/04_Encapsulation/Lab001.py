# Binding data variable with method
# instance variable / data variable can be accessed by only methods

# methods --> by default are function within the class

# wrap our variable / instance variable with the methods --> 04_Encapsulation

# public variable --> any one can access cannot access directly
# protected variable --> members are intended for internal use within the class and its subclasses

class Car:
    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model
        # this is parameterized constructor

    def start_engine(self):
        print(" starting the with name " + self.name)
        print(" starting the with make " + self.make)
        print(" starting the with model " + self.model)
        # this a method

lambo = Car("Lambo", "V6", "2023")

lambo.start_engine()

mg_hector = Car("Hector", "1.5Ltr", "2023")
mg_hector.start_engine()

