import pytest
from student import Student

@pytest.fixture
def std() -> Student:
    """Arrange: Instantiates an independent class body for each test."""
    return Student(name="Saqib Bedar", grade=10)

# test cases

# 1. Test enrollment()
def test_enrollment(std: Student):
    std.enroll("Machine Learning")

    assert "Machine Learning" in std.subjects
    assert len(std.subjects) == 1

# 2. Test upgrade_grade()
def test_upgrade_grade(std: Student):
    std.upgrade_grade()

    assert std.grade == 1
    assert std.name == "Saqib Bedar"
    assert len(std.subjects) == 0
