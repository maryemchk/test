import pytest
from add import add
from multiply import multiply
from divide import divide

def test_add_multiple_cases():
    assert list(add(1, 2)) == [3]
    assert list(add(4, 5)) == [9]
    assert list(add(-1, -2)) == [-3]

def test_multiply_multiple_cases():
    assert list(multiply(10, 2)) == [20.0]
    assert list(multiply(20, 5)) == [100.0]
    assert list(multiply(-50, -10)) == [-500.0]

def test_divide_multiple_cases():
    assert list(divide(10.0, 2.0)) == [5.0]
    assert list(divide(20.0, 5.0)) == [4.0]
    assert list(divide(-50.0, -10.0)) == [5.0]

def test_divide_by_zero():
    with pytest.raises(ArithmeticError):
        divide(10.0, 0.0)