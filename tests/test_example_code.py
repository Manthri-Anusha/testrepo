# tests/test_example_code.py

import pytest
from src.example_code import add, subtract, multiply, divide

@pytest.mark.unit
def test_add():
    """Tests the add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

@pytest.mark.unit
def test_subtract():
    """Tests the subtract function."""
    assert subtract(5, 3) == 2
    assert subtract(10, 10) == 0
    assert subtract(0, 5) == -5

@pytest.mark.unit
def test_multiply():
    """Tests the multiply function."""
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0

@pytest.mark.unit
def test_divide():
    """Tests the divide function."""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    with pytest.raises(ValueError):
        divide(5, 0)  # Division by zero should raise an error

@pytest.mark.integration
def test_combined_operations():
    """Tests a combination of operations."""
    result = add(multiply(2, 3), subtract(10, 5))
    assert result == 11
