test_result = ["PASS", "FAIL", "PASS", "PASS", "FAIL", "SKIPPED"]

pass_give = list(filter(lambda x: x=="PASS", test_result))
print("Test cases which passed :", pass_give)
# expected output: ['PASS', 'PASS', 'PASS']
# explain how filter works here
# filter(lambda x: x=="PASS", test_result) returns a filter object
# we convert the filter object to list using list() function
# filter returns a test result one by one and applies the lambda function to each test result
# if the function returns true for a test result, that test result is included in the final list
# finally we get a list of test results which are "PASS"