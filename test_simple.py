import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (10, 20, 30),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("x, y, result", [
    (5, 6, 30),
    (-7, -8, -36),
])
def test_multiply(x, y, result):
    assert multiply(x, y) == result