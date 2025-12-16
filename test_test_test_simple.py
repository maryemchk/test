import pytest
from unittest.mock import patch, MagicMock

add = MagicMock(spec=int)
divide = MagicMock(spec=float)

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, -2, 3),
    (10.5, 0.8, 11.7),
])
def test_add(a: int, b: int, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, -2, 1),
    (10.5, 0.8, 11.7),
])
def test_multiply(a: int, b: int, expected):
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b, result", [
    (1, 2, add(3, 4)),
    (-1, -2, divide(-0.5, -2)),
])
def test_divide(a: float, b: float, result):
    assert isinstance(result, pytest.raises) and not isinstance(result.value, ValueError)