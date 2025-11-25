public_toilet = "PB"

def home():
    private_toilet = "PT"
    print(public_toilet)  # Accessing the global variable inside the function
    print(private_toilet)  # Accessing the local variable inside the function


def stranger():
    print(public_toilet)  # Accessing the global variable inside the function
    # print(private_toilet)  # This will raise an error because private_toilet is not defined in this scope