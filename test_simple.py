import pytest
from add import add
from multiply import multiply
from divide import divide

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (4, 5, 9),
    (-1, -2, -3)
])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 12.0),
    (20, 5, 25.0),
    (-50, -10, -60.0)
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize("a, b, result", [
    (10.0, 2.0, 20.0),
    (20.0, 5.0, 100.0),
    (-50.0, -10.0, -500.0)
])
def test_divide(a, b, expected):
    assert divide(a, b) == result