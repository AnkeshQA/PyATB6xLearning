class Person:
    def say_name(self,name):
        print("Hi, my name is "+name)
    def say_name(self,name,lastname):
        print("Hi, my name is "+name+" "+lastname)


p = Person()
result = p.say_name("John","Doe")  # This will work
print(result)
