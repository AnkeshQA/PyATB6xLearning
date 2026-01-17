# frequency of characters in a string
# write a program to count the frequency of each character in a string using a dictionary.
# o/p e.g {'a':2,'u':1,'t':2,'o':2,'m':1,'i':1,'n':1}
string = "automation"
string1 = input("\n enter the input e.g automation\n")
char_count = {}  # empty dictionary to store frequency of characters

for char in string1:
    if char in char_count:
        char_count[char] += 1  # increment count if character already in dictionary
    else:
        char_count[char] = 1   # initialize count to 1 if character not in dictionary
print("Frequency of each character in the string is :", char_count)




# another way using char.count() method
string2 = "automation"

char_count2 = {}
for char in string2:
    char_count2[char] = char_count2.get(char, 0)+1
print("Frequency of each characters in the string using char.count() method is :", char_count2)