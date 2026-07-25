# Verify Class Name
class Student:
    def __init__(self):
        pass

# Method 1: using class name directly 
print(Student.__name__)         # Output: Student

# Method 2: Using object/instance
std = Student()
print(std.__class__.__name__)   # Output: Student

# Method 3: using type
print(type(std).__name__)       # Output: Student