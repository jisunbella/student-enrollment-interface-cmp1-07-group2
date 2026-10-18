import random


class Subject:
    def __init__(self, subjectId):
        self.subjectId = subjectId
        self.mark = self.generateMark()
        self.grade = self.calculateGrade()

#305 - mark between 25 and 100
    def generateMark(self):
        return random.randint(25, 100)

#306 - grade from the mark
    def calculateGrade(self):
        if self.mark >= 85:
            return "HD"
        elif self.mark >= 75:
            return "D"
        elif self.mark >= 65:
            return "C"
        elif self.mark >= 50:
            return "P"
        else:
            return "Z"

#subject -> dictionary, students.data에 저장되는 형식이랑 똑같이 {"id", "mark", "grade"}
    def toRecord(self):
        return {
            "id": self.subjectId,
            "mark": self.mark,
            "grade": self.grade
        }
