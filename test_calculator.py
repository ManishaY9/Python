import pytest
from calculator import add, subtract, divide, multiply, modulus, power
def test_add():
    assert add(2,3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 100) == 0

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(5, 0) == "Error: Division by zero"


def test_modulus():
    assert modulus(5, 3) == 2
    assert modulus(10, 2) == 0
    assert modulus(5, 0) == "Error: Modulus by zero"

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(2, -1) == 0.5

# Test add function with multiple inputs
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (5, 10, 15)
])
def test_param_add(a, b, expected):
    assert add(a, b) == expected