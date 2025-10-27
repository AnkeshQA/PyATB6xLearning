"""
simulate a page loading check using a while loop
If page_loaded becomes true within 5 seconds print success else time out
hint : use a counter like wait_time and break condition
"""
page_loaded = False
wait_time = 0

while wait_time < 5:
    user_input = input(f"Second {wait_time + 1}: Has the page loaded? (yes/no): ").lower()

    if user_input == "yes":
        page_loaded = True
        print("Page loaded successfully ✅")
        break

    wait_time += 1

else:
    print("Timeout! Page did not load ❌")
