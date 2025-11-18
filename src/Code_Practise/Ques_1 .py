nums = [1, 2, 4, 5, 6]
n = 6
expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)
missing = expected_sum - actual_sum
print("Missing number:", missing)


"✅ Q1. Create a list of 5 numbers and print the largest and smallest."
nums = [5, 2, 8, 1, 9]
print("Largest:", max(nums))
print("Smallest:", min(nums))
