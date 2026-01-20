import pytest
import allure
import requests

@allure.title("TC#1 verify the get request with valid ID")
@allure.description("verify get request is successful and status code = 200")
@pytest.mark.positive
def test_get_request():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url=url)
    assert response_data.status_code == 200



@allure.title("TC#1 verify the get request with invalid ID")
@allure.description("verify get request is successful and status code = 404")
@pytest.mark.negative
def test_get_request2():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url=url)
    assert response_data.status_code == 404
