pub_toilet ="PB"
def home():
    priv_toilet ="PT"
    print(priv_toilet)  # Accessing the local variable inside the function
    pub_toilet = "LPB"
    print(pub_toilet)  # Accessing the global variable inside the function


home()

# here updated pub_toilet is local variable
# scope of pub_toilet is limited to home function only
# trying to access pub_toilet outside the function will result in an error
print(pub_toilet)  # Accessing the global variable outside the function