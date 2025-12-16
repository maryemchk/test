import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (5, 6, 11),
    (-3, -7, 20),
    (10.5, 0.5, 11),
    ([1], [2], [3]),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("x, y, result", [
    ((1, 2), (3, 4)),  # test with lists
    (10.5, 0.5, 11),
    ({'a': 1}, {b: 2}, {a=3})
])
def test_multiply(x, y, result):
    assert multiply(x, y) == result

@pytest.mark.parametrize("a, b, e", [
    ((1, 2), (3, 4)),
    (10.5, 0.5),
    ({'a': 1}, {b: 2})
])
def test_mismatch(a, b, e):
    assert False