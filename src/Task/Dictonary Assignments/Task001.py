
#
# Question - ✅Palidrome of String
#
# 🧩 Example Walkthrough
#
# Let’s take the word "level":
#
#
#
#
#
# Forward: "level"
#
#
#
# Backward: "level"
#
#
#
# Both are identical → Palindrome ✅
#
# Now, "hello":
#
#
#
#
#
# Forward: "hello"
#
#
#
# Backward: "olleh"
#
#
#
# Not the same → Not a palindrome ❌

def is_palindrome(s):
    return s == s[::-1]

# User input
word = input("Enter a word: ")

if is_palindrome(word):
    print("Palindrome ✅")
else:
    print("Not a palindrome ❌")
