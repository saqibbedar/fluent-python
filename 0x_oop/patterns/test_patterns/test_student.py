from student import Student

# 1. Helper function (factory pattern/factory function)
# return new/fresh instance on each function call
def make_fresh_student() -> Student:
    return Student(name="placeholder", grade=10)

# 2. Independent Test Function 1
def test_enrollment():
    # Arrange: Call the helper to get an isolated instance
    dummy_user_instance = make_fresh_student()

    # Act
    dummy_user_instance.enroll("Machine Learning")

    # Assert
    assert "Machine Learning" in dummy_user_instance.subjects

# 3. Independent Test Function 2
def test_grade_upgrade():
    # Arrange: Call the helper again. This instance is 100% separate from the one above!
    dummy_user_instance = make_fresh_student()

    # Act
    dummy_user_instance.upgrade_grade()

    # Assert
    assert dummy_user_instance.grade == 11
    assert len(dummy_user_instance.subjects) == 0       # Isolation test: no subject in this instance
