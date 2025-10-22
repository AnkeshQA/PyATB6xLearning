"""
check if user can log in based on correct username and password
username = "admin"
password = "1234"
o/p
login successful

o/p
invalid creds
"""
name = input("enter username\n").strip()
pwd = input("enter pwd\n").strip()
username = "admin"
password = "1234"

if username.strip() == name.strip() and password.strip()== pwd.strip():
    print("valid details")
else:
    print("enter valid details")
