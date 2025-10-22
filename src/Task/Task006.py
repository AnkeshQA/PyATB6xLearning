"""
in an automation code you often compare expected and actual outputs
write a code to if test case is passed or failed
expected_title = "Dashboard"
actual ="Dashboard"
print test case passed
print title mismatched
user lower case and strip
"""
expected_title = "Dashboard"
actual ="dashboard "
if expected_title.strip().lower() == actual.strip().lower():
    print("test case passed")
else:
    print("title mismatched")