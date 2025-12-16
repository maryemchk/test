import pytest

def test_add():
    assert add(1, 2) == 3
    assert add(-1, -2) == -3
    with pytest.raises(TypeError):
        add('a', 2)

def test_multiply():
    assert multiply(5, 6) == 30
    assert multiply(-5, -6) == 30
    assert multiply(0, 10) == 0

def test_multiply_with_non_integers():
    with pytest.raises(TypeError):
        multiply(1.5, 2)
    with pytest.raises(TypeError):
        multiply('a', 2)

def test_add_with_zero():
    assert add(0, 0) == 0
    assert add(-1, -1) == 0