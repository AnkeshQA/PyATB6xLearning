def validate_status_code(response_code):
    """Validate if the response code is 200."""
    if response_code > 0:
        if response_code == 200:
            print("Valid response code:", response_code)
        else:
            print("Invalid response code:", response_code)
    else:
        print("Please enter a positive response code.")

validate_status_code(200)  # Valid
validate_status_code(404)  # Invalid
