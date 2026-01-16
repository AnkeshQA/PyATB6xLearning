# remove empty strings from a list of strings
data = ["apple", "", "banana", "cherry", "", "date", ""]
non_empty = list(filter(None,data))
print(non_empty)


def non_empty_string(s):
    if s!="":
        return True
    return None