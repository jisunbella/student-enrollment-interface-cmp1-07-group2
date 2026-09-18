import json
from pathlib import Path

from student import Student 

class Database: 
    def __init__(self, dataFile = None):
        self.dataFile=(
            Path(dataFile)
            if dataFile is not None 
            else Path(__file__).with_name("Students.data")
        )
        if not self.dataFile.exists():
            self.saveStudent([])

#save Sutdnet Inoforamation 
    def saveStudent(self,studentsInfo):
        data =[]

        for student in studentsInfo:
            data.append(student.toRecord())

# generating the temporary file (draft) to add the student infromation.-> replace it to the actual dataFile  
        tempFile =self.dataFile.with_name(
            self.dataFile.name + ".temp"
        )
        with tempFile.open ("w",encoding ="utf-8") as file:
            json.dump(data, file)
        tempFile.replace(self.dataFile)

#bring the student data as the reader mode 
    def loadStudents(self):
        with self.dataFile.open("r", encoding="utf-8") as file:
            data = json.load(file)

        studentsInfo = []
        for item in data:
            student = Student.fromRecord(item)
            studentsInfo.append(student)

        return studentsInfo
    




