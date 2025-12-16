```
import pytest
from add import add
from multiply import multiply
from divide import divide

def test_add_case():
    assert add(1, 2) == 3
    assert add(-1, -2) == -3
    assert add(-10, -5) == -15

@pytest.mark.parametrize("a, b", [
    (1.0, 2.0),
    ("1, 2", " -> 3")
])
def test_multiply_case(a, b):
    result = multiply(a, b)
    assert isinstance(result, tuple)

def test_divide_case():
    with pytest.raises(ZeroDivisionError):
        divide(-10, -5)
    with pytest.raises(TypeError):
        divide("a", 2)

if __name__ == "__main__":
    pytest.main()