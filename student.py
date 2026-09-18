class Student:
    def __init__(self, name, email, password, studentId, subjects=None):
        self.name = name
        self.email = email
        self.password = password
        self.studentId = studentId
        self.subjects = subjects if subjects is not None else []

