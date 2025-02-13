import pytest
from Assingment6_Target_code import Calculator  # Import the Calculator class

@pytest.fixture
def calc():
    
    return Calculator()

def test_add(calc):
    assert calc.add(3, 2) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

def test_subtract(calc):
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(10, 20) == -10
    assert calc.subtract(-5, -5) == 0

def test_multiply(calc):
    assert calc.multiply(3, 3) == 9
    assert calc.multiply(-1, 5) == -5
    assert calc.multiply(0, 10) == 0

def test_divide(calc):
    assert calc.divide(10, 2) == 5
    assert calc.divide(9, 3) == 3
    assert calc.divide(1, 1) == 1
    assert calc.divide(0, 5) == 0
    assert calc.divide(5, 0) == "Error! Division by zero."

def test_power(calc):
    assert calc.power(2, 3) == 8
    assert calc.power(5, 0) == 1
    assert calc.power(7, 1) == 7
    assert calc.power(4, -1) == 0.25

