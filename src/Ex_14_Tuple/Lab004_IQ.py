cities = ("New York", "Los Angeles", "Chicago", "Houston", "Phoenix")
print(len(cities))
print("paris" in cities)
print("Chicago" in cities)

# tuple cannot be modified, but we can create a new tuple by concatenation

colors = ("Red", "Green", "Blue")
for c in colors:
    print(c)

numbers =(1,2)*3
print(numbers)
# java will not allow this but python allows this

nums = (10, 20, 30, 40, 50,20,30,20)
print(len(nums))
print(nums.count(20))
print(nums.index(30))

#minimum and maximum in tuple
print(min(nums))
print(max(nums))
print(sum(nums))

# slicing in tuple
print(nums[1:5])
print(nums[-1])
print(nums[-3])
print(nums[-5:-1])