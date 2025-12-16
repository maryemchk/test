import pytest
from add import add
from multiply import multiply
from divide import divide

@pytest.mark.parametrize("a, b", [
    (1, 2),
    (10, 5),
    (-1, -2)
])
def test_add_case(a, b):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b", [
    (1.0, 2.0),
    "(1, 2) -> 3"
])
def test_multiply_case(a, b):
    result = multiply(a, b)
    assert isinstance(result, tuple)

@pytest.mark.parametrize("a, b, e", [
    (-1.0, -2.0, ValueError),
    (10.0, 5.0, None)
])
def test_divide_case(a, b, expected):
    with pytest.raises(expected):
        divide(a, b)