# check vowels in a string

input_string = "hello world!"
# a,e,i,o,u

vowels = "aeiou"

vowels_count = 0
results = dict()

for char in input_string:
    if char in vowels:
        vowels_count += 1
print(vowels_count)


# show vowels in a string

string2 ="uueoondhsikjshuwjmlopwpedb"
vowels = "aeiou"

vowels_count = 0
results = list()

for char in input_string:
    if char in vowels:
        vowels_count += 1
        results.append(char)
print(vowels_count)
print(results)




