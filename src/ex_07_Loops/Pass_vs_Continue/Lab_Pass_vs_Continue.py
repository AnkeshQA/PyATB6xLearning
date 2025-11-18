for i in range (5):
    if i ==3:
        pass  # Placeholder for future code when i is 3
    print("number: ",i) # this line will always execute



for i in range (5):
    if i ==3:
        continue  # Skip the rest of the loop when i is 3
    print("number: ",i) # this line will always execute
# Output will be
# number:  0
# number:  1
# number:  2
# number:  4

