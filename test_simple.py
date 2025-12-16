import pytest
from add import add
from multiply import multiply
from divide import divide

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (10, 5, 15),
    (-1, -2, -3)
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (1.0, 2.0, 2.0), "(1, 2) -> 3"
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b, e", [
    (-1.0, -2.0, ValueError),
    (10.0, 5.0, None)
])
def test_divide(a, b, e):
    with pytest.raises(e):
        divide(a, b)