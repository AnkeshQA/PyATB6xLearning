class Mathclass:
    def add (self,a,b):
        return a + b # this method will be overridden by the next one, and it is not getting called

    def add (self,a,b,c=10): # default value of c given for method overloading
        return a+b+c


obj_reference = Mathclass()
result = obj_reference.add(5,10,20)
result2 = obj_reference.add(6.5,10.5)

print(result)
print(result2)

# explanation: In Python, method overloading is not natively supported as in some other languages.
# here latest function definition will override the previous one.

