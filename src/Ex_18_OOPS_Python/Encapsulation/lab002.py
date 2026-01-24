class VWOLoginPage:


    def __init__(self,email_args,pwd_args):
        self.email = email_args
        self.password = pwd_args

    def login_confirm(self):
        if self.email == "pramod@gmail.com"and self.password == "Ankesh123":
            print("Login Successful")
        else:
            print("Login Failed")


email = input(" enter the vwo email")
password = input(" enter the vwo password")

vwo_object_ref = VWOLoginPage(email,password)
vwo_object_ref.login_confirm()