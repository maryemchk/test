import pytest

def add(a: int, b: int) -> int:
    assert isinstance(a, int), "Input must be an integer"
    assert isinstance(b, int), "Input must be an integer"
    return a + b

def multiply(a: int, b: int) -> int:
    assert isinstance(a, int), "Input must be an integer"
    assert isinstance(b, int), "Input must be an integer"
    return a * b

def divide(a: float, b: float) -> float:
    assert isinstance(a, (int, float)), "Input must be a number"
    assert isinstance(b, (int, float)), "Input must be a number"
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 2) == -1
    assert add(-1, -2) == -3

def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-4, 5) == -20
    assert multiply(-4, -5) == 20

def test_divide():
    assert divide(10.0, 2.0) == 5.0
    assert divide(10.0, 0.0) is None
    assert divide(1.0, 0.0) is None

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10.0, 0.0)

def test_add_floats():
    assert add(1.5, 2.5) == 4.0
    assert add(-1.5, -2.5) == -3.5

def test_multiply_floats():
    assert multiply(4.0, 5.0) == 20.0
    assert multiply(-4.0, 5.0) == -20.0
    assert multiply(-4.0, -5.0) == 20.0

def test_divide_floats():
    assert divide(10.0, 2.0) == 5.0
    assert divide(10.0, 0.0) is None
    assert divide(1.0, 0.0) is None

def test_divide_by_zero_floats():
    with pytest.raises(ValueError):
        divide(10.0, 0.0)

def test_add_negative_integers():
    assert add(-1, -2) == -3

def test_multiply_negative_integers():
    assert multiply(-4, -5) == 20
    assert multiply(-4, -1) == -4

def test_divide_negative_integers():
    with pytest.raises(ValueError):
        divide(10.0, -2.0)

def test_add_string():
    with pytest.raises(TypeError):
        add("hello", 2)
    try:
        add(3.5, "hello")
    except TypeError as e:
        assert str(e) == "Input must be an integer or a number"

def test_multiply_string():
    with pytest.raises(TypeError):
        multiply("hello", 2)
    try:
        multiply(3.5, "hello")
    except TypeError as e:
        assert str(e) == "Input must be a number"

def test_divide_string():
    with pytest.raises(TypeError):
        divide("hello", 2)
    try:
        divide(3.5, "hello")
    except TypeError as e:
        assert str(e) == "Input must be a number"