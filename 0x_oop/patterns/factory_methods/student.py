class Student:
    def __init__(self, name: str = "", grade: int = 0) -> None:
        self.name = name
        self.grade = grade
        self.subjects = []

    def enroll(self, subject: str) -> None:
        self.subjects.append(subject)

    def upgrade_grade(self, grade: int) -> None:
        self.grade = grade