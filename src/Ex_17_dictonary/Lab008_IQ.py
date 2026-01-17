# write a program which return maximum and minimum value from a dictionary
# e.g input_dict = {'a':100,'b':200,'c':50,'d':300}
# o/p - max value is 300 , min value is 50

input_dict = {'a':100,'b':200,'c':50,'d':300}
def max_value(input_dict):
    max_val = max(input_dict.values())
    return max_val
def min_value(input_dict):
    min_val = min(input_dict.values())
    return min_val
print("Maximum value in the dictionary is :", max_value(input_dict))
print("Minimum value in the dictionary is :", min_value(input_dict))


# find minimum key in the dictionary based on its value
# e.g input_dict = {'a':100,'b':200,'c':50,'d':300}
# o/p - min key is 'c' with value 50
def min_key(input_dict):
    min_key = min(input_dict, key=input_dict.get)
    return min_key
print("Minimum key in the dictionary based on its value is :", min_key(input_dict))
