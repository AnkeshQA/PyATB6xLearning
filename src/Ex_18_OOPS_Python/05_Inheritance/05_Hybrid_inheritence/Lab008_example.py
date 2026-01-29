# Hybrid inheritance : mixture of multiple and multilevel inheritance

class Base:
    def base_method(self):
        print("Base method called")

class A(Base):
    def a_method(self):
        print("A method called")
class B(Base):
    def b_method(self):
        print("B method called")

class C(A,B):
    def c_method(self):
        print("C method called")

obj = C()
obj.a_method()
obj.b_method()
obj.c_method()