import pytest
from typing import ParamType, TypeVar, Optional

T = TypeVar('T')

def add(a: T, b: T) -> T:
    """Return the sum of two integers."""
    return a + b

def multiply(a: T, b: T) -> T:
    """Return the product of two integers."""
    return a * b

def divide(a: float, b: float) -> Optional[float]:
    """Return a / b. Raise ValueError if b == 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b