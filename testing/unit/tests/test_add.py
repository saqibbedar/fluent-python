from unit.Math.add import add

# Test Cases


# Test 1
def test_positive_numbers():
    assert add(5, 20) == 25


# Test 2
def test_negative_numbers():
    assert add(-10, -10) == -20


# Test 3
def test_zero():
    assert add(17, 0) == 17
