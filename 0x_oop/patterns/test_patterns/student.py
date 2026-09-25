class Student:
    def __init__(self, name: str, grade: int):
        self.name = name
        self.grade = grade
        self.subjects = []

    def enroll(self, subject_name: str) -> None:
        self.subjects.append(subject_name)

    def upgrade_grade(self) -> None:
        self.grade += 1

