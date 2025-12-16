import pytest

def test_add():
    assert add(1, 2) == 3
    assert add(-1, -2) == -3
    assert add(0, 0) == 0

def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(-1, -2) == 2
    assert multiply(0, 0) == 0

def test_invalid_input_add():
    with pytest.raises(TypeError):
        add('a', 2)
    with pytest.raises(TypeError):
        add(1, 'b')

def test_invalid_input_multiply():
    with pytest.raises(TypeError):
        multiply(-1, 'x')
    with pytest.raises(TypeError):
        multiply(0, -1)

def test_add_multiple_calls():
    assert add(1, 2) == 3
    add(2, 3)
    assert add(1, 2) == 3

def test_multiply_multiple_calls():
    assert multiply(1, 2) == 2
    multiply(2, 3)
    assert multiply(1, 2) == 2