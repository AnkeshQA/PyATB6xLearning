"""
you want to check whether a web page load within 3 seconds (performance test condition)
load time = 4.2
o/p page is too slow 4.2 seconds
"""

load_time = float(input("enter load time for the page"))
if load_time <=3:
    print("page loading successful",{load_time})
else:
    print("load time exceeded")
