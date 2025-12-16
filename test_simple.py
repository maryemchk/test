import pytest

def test_add_valid_cases():
    assert add(2, 3) == 5
    assert add(-1, 4) == -5
    assert add(0, 0) == 0

@pytest.mark.parametrize("a, b, expected", [
    (-2, 2, 0),
    (10, -5, 2),
    (3.14, 2, 1.57)
])
def test_add_invalid_cases(a, b, expected):
    with pytest.raises(ValueError):
        add(a, b)

def test_multiply_valid_cases():
    assert multiply(4, 5) == 20
    assert multiply(-6, -7) == 42
    assert multiply(9, 3.14) == 28.26

@pytest.mark.parametrize("a, b, expected", [
    (2, 0, 1),
    (-10, 3, -13)
])
def test_multiply_invalid_cases(a, b, expected):
    with pytest.raises(ValueError):
        multiply(a, b)

def test_divide_valid_cases():
    assert divide(10, 2) == 5.0
    assert divide(-11, 1) == -11.0
    assert divide(9.14, 3.14) == 2.9000305173741878

@pytest.mark.parametrize("a, b, expected", [
    (4, 0, float('inf')),
    (-10, 3, -33.333333333333332)
])
def test_divide_invalid_cases(a, b, expected):
    with pytest.raises(ValueError):
        divide(a, b)