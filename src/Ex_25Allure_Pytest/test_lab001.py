#install allure-pytest
# pip install allure-pytest

import allure
import pytest


@allure.title("Verify create booking - negative scenario")
@allure.description("Verify create booking fails with invalid data")
@pytest.mark.negative
def test_method1():
    print("hello world")
    assert 4 - 1 == 5   # expected failure


@allure.title("Verify login - positive scenario")
@allure.description("Verify login works with valid credentials")
@pytest.mark.positive
def test_login():
    print("hello worlds")
    assert 1 + 1 == 2
