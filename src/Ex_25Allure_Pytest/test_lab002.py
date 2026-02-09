import pytest
import allure
@allure.title("TC#1 verify 2-2 == 0")
@allure.description("basic maths")
@pytest.mark.negative
def test_method1():
    print("hello world")
    assert 2 - 2 == 0   # expected failure




@pytest.mark.skip(reason="skip")
def test_method2():
    print("hello skipped world")
    assert 0 - 0 != 0   # expected failure