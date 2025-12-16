import pytest
from add import add
from multiply import multiply
from divide import divide

@pytest.mark.parametrize("a, b", [
    (1, 2),
    (-1, -3),
    (0.5, 4.25),
    (10, -20)
])
def test_add(a: int, b: int):
    assert add(a, b) == a + b

@pytest.mark.parametrize("a, b", [
    (1, 2),
    (-1, -3),
    (0.5, 4.25),
    (10, -20)
])
def test_multiply(a: int, b: int):
    assert multiply(a, b) == a * b

@pytest.mark.parametrize("a, b", [
    (1.0, 2.0),
    (-1.0, -3.0),
    (0.5, 4.25),
    (10.0, -20.0)
])
def test_divide(a: float, b: float):
    assert divide(a, b) == a / b