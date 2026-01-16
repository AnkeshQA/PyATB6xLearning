# Question - ✅ Count vowels and consonants in a String

def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in s:
        if char.isalpha():  # Check only letters
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count


# User input
word = input("Enter a string: ")

vowels, consonants = count_vowels_consonants(word)

print("Vowels:", vowels)
print("Consonants:", consonants)
