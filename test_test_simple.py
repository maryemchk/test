import pytest

@pytest.mark.parametrize("a, b, expected", [
    ({1, 2}, {3, 4}, {(1, 2), (3, 4)}),
    ({10, 20}, {30, 40}, {(10, 20), (30, 40)}),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("x, y, result", [
    ({5, 6}, {7, 8}, {(5, 6), (7, 8)}),
    ({-7, -8}, {-9, -10}, {(-7, -8), (-9, -10)}),
])
def test_multiply(x, y, result):
    assert multiply(x, y) == result