import pytest

def test_add_valid_cases():
    assert add(2, 3) == 5
    assert add(-1, 4) == -5
    assert add(0, 0) == 0
    with pytest.raises(ValueError):
        add(-2, 2)
    with pytest.raises(ValueError):
        add(10, -5)

def test_multiply_valid_cases():
    assert multiply(4, 5) == 20
    assert multiply(-6, -7) == 42
    assert multiply(9, 3.14) == 28.26
    with pytest.raises(ValueError):
        multiply(-2, 2)
    with pytest.raises(ValueError):
        multiply(10, -5)

def test_multiply_invalid_cases():
    with pytest.raises(ValueError):
        multiply(0, 0)
    with pytest.raises(ValueError):
        multiply(4, -5)

def test_divide_valid_cases():
    assert divide(10, 2) == 5.0
    assert divide(-11, 1) == -11.0
    assert divide(9.14, 3.14) == 2.9000305173741878
    with pytest.raises(ValueError):
        divide(4, 0)
    with pytest.raises(ValueError):
        divide(10, -5)

def test_divide_invalid_cases():
    with pytest.raises(ValueError):
        divide(0, 0)
    with pytest.raises(ValueError):
        divide(9.14, -3.14)