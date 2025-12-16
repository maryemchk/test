import pytest

@pytest.mark.parametrize('a: int, b: int, expected_result',
                    [(1, 2, 3),
                     (2, 3, 6),
                     (-1, 1, -1.0),
                     (-1, -1, 1.0)],
                    indirect=True)
def test_add(a, b, expected_result):
    assert add(a, b) == expected_result

@pytest.mark.parametrize('a: float, b: float, expected_result',
                    [(1.0, 2.0, 3.0),
                     (2.0, 3.0, 6.0)],
                    indirect=True)
def test_multiply(a, b, expected_result):
    assert multiply(a, b) == expected_result

@pytest.mark.parametrize('a: int, b: int, expected_result',
                    [(-1, 1, -1), (-1, -1, 1)],
                    indirect=True)
def test_divide(a, b, expected_result):
    assert divide(a, b) == expected_result