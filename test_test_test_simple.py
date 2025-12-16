import pytest
from unittest import skipIf  # noqa: F401
from typing import Callable, Any

@pytest.mark.parametrize('a, b', [
    (1, 2),
    (-1, -2)
], skipper=True)
def test_add(a: int, b: int):
    assert add(a, b) == a + b


@pytest.mark.parametrize('a, b', [
    (1, 2),
    (-1, -2),
], skipper=True)
def test_multiply(a: int, b: int):
    assert multiply(a, b) == a * b


@skipIf(True, "Cannot divide by zero")
def test_divide(a: float, b: float):
    assert divide(a, b) == a / b