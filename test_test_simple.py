import pytest

@pytest.mark.parametrize('a: int, b: int', [(1, 2), (2, 3)])
def test_add(a, b):
    assert add(a, b) == a + b

@pytest.mark.parametrize('a: float, b: float', [(1.0, 2.0), (2.0, 3.0)])
def test_multiply(a, b):
    assert multiply(a, b) == a * b

@pytest.mark.parametrize('a: int, b: int', [(-1, 1), (-1, -1)])
def test_divide(a, b):
    assert divide(a, b) == a / b