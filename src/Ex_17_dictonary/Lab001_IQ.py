# frequency of characters in a string
# write a program to count the frequency of each character in a string using a dictionary.

string = "automation"
string = input("\n enter the input e.g automation\n")

#logic building to count frequency of each character
# in/p - string e.g "automation"
# out/p - dictionary e.g {'a':2,'u':1,'t':2,'o':2,'m':1,'i':1,'n':1}
frequency = {}  # empty dictionary to store frequency of characters
for char in string:
    if char in frequency:
        frequency[char] += 1  # increment count if character already in dictionary
    else:
        frequency[char] = 1   # initialize count to 1 if character not in dictionary
print("Frequency of each character in the string is :", frequency)