#assertion --> check expected result with actual result
# keyword : assert a == a
import pytest


@pytest.mark.regression
def test_method1():
    print("hello world")
    assert 4-1 == 6

# every function we create is a test case

pytest.mark.smoke
def test_method2():
    print("hello world")
    assert 1+1 ==2


