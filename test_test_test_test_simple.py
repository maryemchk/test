import pytest
from unittest.mock import patch, MagicMock
from typing import Callable

add = MagicMock(spec=int)
divide = MagicMock(spec=float)

@pytest.mark.parametrize("a, b", [
    (1, 2),
    (-1, -2),
])
def test_add(a: int, b: int):
    result = add(a, b)
    assert isinstance(result, int)

@pytest.mark.parametrize("a, b", [
    (1, 2),
    (-1, -2),
])
def test_multiply(a: int, b: int):
    result = multiply(a, b)
    assert isinstance(result, float)

def multiply(a: int, b: int) -> float:
    return a * b

@pytest.mark.parametrize("a, b", [
    (1, 2.5),
    (-1, -2.5),
])
def test_multiply_negative(a: int, b: float):
    result = multiply(a, b)
    assert isinstance(result, pytest.raises) and not isinstance(result.value, ValueError)

def divide(a: float, b: float) -> float:
    return a / b

@pytest.mark.parametrize("a, b", [
    (1, 2.5),
    (-1, -2.5),
])
def test_divide_negative(a: float, b: float):
    with pytest.raises(ZeroDivisionError):
        divide(a, b)

def test_multiply_zero(a: int, b: float) -> None:
    result = multiply(a, 0)
    assert isinstance(result, float)

def test_multiply_nonzero(a: int, b: int) -> None:
    result = multiply(a, b)
    assert isinstance(result, float)