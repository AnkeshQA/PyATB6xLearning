response = [1200,1800,2400,3000,3600]

def mil_sec(x):
    return x /1000
res = list(map(mil_sec, response))
print("Response time in seconds :", res)
# expected output: [1.2, 1.8, 2.4, 3.0, 3.6]
# explain how map works here
# map(mil_sec, response) returns a map object
# we convert the map object to list using list() function
# map returns a response time one by one and applies the function mil_sec to each response time
# finally we get a list of response times in seconds
# x