def vwo_login(user):
    if user != "admin":
        raise Exception("Unauthorized Access!!") # using keyword raise we can throw an exception
    return "Welcome Admin"

print(vwo_login("pramod"))
print(vwo_login("admin"))

#You can also create your **custom exception by using or creating a cla**ss
#
# class InvalidAgeException(Exception):
#  pass
# 
# def can_you_drink(age):
#  if age < 18:
#  raise InvalidAgeException("Invalid age of drinking")
#
# can_you_drink(17)
# can_you_drink(25)
#
