def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def multiply(a: int, b: int) -> int:
    """Return the product of two integers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a / b. Raise ValueError if b == 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
