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
max_attempts = 3
while attempt <= max_attempts:
    response = int(input(f"attempt {attempt}: enter your response code\n").strip())
    if response == 200:
        print("test passed")
        break
    else:
        print(f"attempt {attempt}: response code {response}")
    attempt += 1
if attempt > max_attempts and response != 200:
    print("test failed after 3 attempts")