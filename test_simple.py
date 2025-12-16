import pytest

@pytest.mark.parametrize('a, b', [(1, 2), (2, 3)])
def test_add(a: int, b: int):
    assert add(a, b) == a + b

@pytest.mark.parametrize('a, b', [(1.0, 2.0), (2.0, 3.0)])
def test_multiply(a: float, b: float):
    assert multiply(a, b) == a * b

@ pytest.mark.parametrize('a, b', [(-1, 1), (-1, -1)])
def test_divide(a: int, b: int):
    assert divide(a, b) == a / b