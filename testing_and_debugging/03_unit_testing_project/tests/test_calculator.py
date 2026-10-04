import pytest
from unit.Math.calculator import Calculator


@pytest.fixture
def calc() -> Calculator:
    """Arrange: Instantiates an independent class body for each test."""
    return Calculator()


# Test 1. addition
def test_addition(calc: Calculator):
    assert calc.add(10, 10) == 20
    assert calc.add(-3, -7) == -10
    assert calc.add(5, 0) == 5
    assert calc.add(0, 5) == 5


# Test 2. subtraction
def test_subtraction(calc: Calculator):
    assert calc.sub(20, 10) == 10
    assert calc.sub(-10, -10) == 0
    assert calc.sub(10, 0) == 10
    assert calc.sub(0, 10) == -10


# Test 3. multiplication
def test_multiplication(calc: Calculator):
    assert calc.mul(10, 10) == 100
    assert calc.mul(5, -5) == -25
    assert calc.mul(-5, -5) == 25
    assert calc.mul(5, 0) == 0


# Test 4. division
def test_division(calc: Calculator):
    assert calc.div(2, 2) == 1
    assert calc.div(10, 2) == 5
    assert calc.div(-5, 5) == -1
    assert calc.div(5, -5) == -1
    assert calc.div(-10, -10) == 1


# Test 5. division by zero
def test_division_by_zero(calc: Calculator):
    """Clean syntax"""
    with pytest.raises(ZeroDivisionError):
        calc.div(1, 0)


# Another way to perform it
# def test_division_by_zero(calc: Calculator):
#     pytest.raises(ZeroDivisionError, calc.div, 1, 0)
