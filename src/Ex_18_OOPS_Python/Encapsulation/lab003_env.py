from dotenv import load_dotenv # created by python community

import os  # created by python guys


class VWOLoginPage:


    def __init__(self,email_args,pwd_args):
        self.email = email_args
        self.password = pwd_args

    def login_confirm(self):
        load_dotenv() #calling the function
        if self.email == os.getenv("USERNAME") and self.password == os.getenv("PASSWORD"):
            print("Login Successful")
        else:
            print("Login Failed")


email = input(" enter the vwo email")
password = input(" enter the vwo password")

vwo_object_ref = VWOLoginPage(email,password)
vwo_object_ref.login_confirm()

# using os.getenv will fetch us the username and password from dotenv file