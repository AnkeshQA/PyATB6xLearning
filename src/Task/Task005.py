"""
you receive an PAI response code from your test scripts
write an if else block to check whether the is successful status code 200 or not

o/p failed api attempt and response code 404
o/p response 200 api passed attempt
"""



api_response =int(input("enter your response code\n").strip())

if api_response == 200:
    print("the api response is valid")
elif api_response == 404:
    print("API response failed")
else:
    print("enter valid response within 2xx to 5xx")

