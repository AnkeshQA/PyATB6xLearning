"""
AN api fails sometime due to network delays
write a program to retry the API call 3 times until the response code becomes 200. If it still fails after 3 tries print
a failure message

hint : use a while loop with a counter
attempt 1: response code 500
attempt 2 : response code 200
test passed 
"""
attempt = 1
response = 0

while attempt <= 3:
    # Simulate API response manually
    # You can change this value to test (e.g., 500, 404, 200)
    response = int(input(f"Enter response code for Attempt {attempt}: "))

    print(f"Attempt {attempt}: Response {response}")

    if response == 200:
        print("API call successful ✅")
        break

    attempt += 1

if response != 200:
    print("API failed after 3 attempts ❌")
