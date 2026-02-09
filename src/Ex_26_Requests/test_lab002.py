import pytest
import requests
import allure

@allure.title("TC#1 - create booking CURD positive")
@allure.description("verify the create booking is successful and status code = 200")
@pytest.mark.curd
def test_create_booking_positive_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    full_url = base_url + base_path

    headers = {"Content-Type": "application/json"}
    payload = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    response_data = requests.post(full_url, headers=headers, json=payload)
    print(response_data.text)

    assert response_data.status_code == 200

    #booking id > 0 and first name name is jim
