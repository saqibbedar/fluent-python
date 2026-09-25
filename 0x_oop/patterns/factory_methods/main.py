from student import Student

# Factory function
def make_student(name: str="", grade: int=0) -> Student:
    new_std = Student(name=name, grade=grade)
    return new_std

# 1. Caching it in a variable
std1 = make_student("Saqib Bedar", grade=10)
std1.enroll("AI")
print(std1.name)        # Output: Saqib Bedar

# 2. Inline chaining (No variable assignment)
std_name = make_student(name="Dur Muhammad").name
print(std_name)    # Output: Dur Muhammad