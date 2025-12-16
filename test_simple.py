import pytest
from add import add
from multiply import multiply
from divide import divide

def test_add_zero():
    assert add(1, 0) == 1
    assert add(0, 1) == 1

def test_add_positive():
    assert add(5, 2) == 7
    assert add(-3, -4) == -7

def test_add_negative():
    assert add(-5, -2) == -7
    assert add(0, -1) == -1

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, -3) == 6
    assert multiply(4, 5) == 20

def test_multiply_zero():
    assert multiply(2, 0) == 0
    assert multiply(0, 2) == 0
    assert multiply(-2, 0) == 0

def test_multiply_negative():
    assert multiply(-2, -3) == 6
    assert multiply(-4, -5) == 20
    assert multiply(0, -1) == 0

def test_divide_positive():
    assert divide(10, 2) == 5.0
    assert divide(15, 3) == 5.0
    assert divide(-5, 0) == ValueError("Cannot divide by zero")

def test_divide_negative():
    assert divide(-20, -4) == 5.0
    assert divide(-35, -5) == 7.0
    assert divide(0, 0) == float('inf')

def test_divide_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
    with pytest.raises(ValueError):
        divide(15, 3)