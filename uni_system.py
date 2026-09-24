
#Student data format 
import email
import json
import random #student ID generation
import re #email and password validation
from pathlib import Path

from student import Student

class UniApp:
#University System requiremnt, choosing the subsystem class. 
    def universitySystem(self):
        while True:
            print("\nWelcome to the University System. please choose a following option")
            print(" (A) Admin")
            print(" (S) Student")
            print(" (X) Exit")
            choice = input("Enter your choice (A-S-X): ")

            # Todo: 대소문자 구분 없이 하는게 나을 것 같아요! (입력받은 문자를 대문자로 통일)
            if choice == 'A': 
                print("Please login as an admin, otherwise Please choose a different option.")
            elif choice == 'S':
                self.studentSystem ()
            elif choice == 'X':
                print("Exiting the UniApp. Goodbye!")
                break
            else:
                print("Invalid. Please try again.")

#The Student subsystem menu, which includes login and registration functionalities for students.
    def studentSystem(self):
        while True:
            print("\n Welsome to the Student System. please choose a following option:")
            print(" (l) login")
            print(" (r) register")
            print(" (x) exit")
            choice = input("Enter your choice (l-r-x): ")

            # Todo: 대소문자 구분 없이 하는게 나을 것 같아요! (입력받은 문자를 대문자 또는 소문자로 통일)
            if choice == 'l':
                self.loginStudent ()
            elif choice == 'r':
                self.registerStudent ()
            elif choice == 'x':
                print("Exiting the Student System.")
                break
            else:
                print("Invalid. Please try again.")


#Student Registration functionality.
    def registerStudent(self):
        print("\n Welcome to the Student Registration System")
        while True:
            name = input("Enter your name: ") 
            if name:
                break
            else:
                print("Wrong access. Name cannot be empty. Please try again.")
            
        while True:
            email = input("Enter your email (name@university.com): ") # Todo: firstname.lastname@university.com
            if self.validateEmail(email):
                break
            else:
                print("""Wrong access. Enter a valid email address
                name@university.com""")

        while True:
            password = input("Enter your password (Password123): ")
            if self.validatePassword(password):
                break
            else:
                print("""Wrong access. Please follow the password format.
                Password required
                - Must start with anUppercase Letter
                - Contain at least 5-letter
                - Contain at least 3-digit Please try again.""")

        print("""Registration successful!, 
        please back to the student system and login with your email and password.""")
        print(f"Your student ID is: {self.generateStudentId()}")
        
#validation for email and password format
    def validateEmail(self, email): #email
        pattern = r"[^@\s]+@university\.com" 
        # Todo: email format: firstname.lastname@university.com
        # 현재 특수문자 입력이 허용돼서 아이디 부분 "문자.문자" 형식만 입력 가능하도록 validation 수정
        return bool(re.fullmatch(pattern, email))

    def validatePassword(self, password): #password
        pattern = r"[A-Z][A-Za-z]{4,}[0-9]{3,}" # Todo: password format이 현재는 대문자 + 영문4글자 + 숫자3자리로 고정되어있는데, 대문자 시작 부분만 고정하고 뒤에는 영문, 숫자 입력 순서 상관없이 가능하도록 수정 필요 
        return bool(re.fullmatch(pattern, password))
    
#Auto-student ID generation 
    def generateStudentId(self):
        existingIds = {student.studentId for student in self.students}
        while True: 
            studentID = str(random.randint(100000, 999999)).zfill(6) # Todo: 해당 부분은 100000~999999로 되어 있어서 1~999999로 수정 필요합니다!
            if studentID not in existingIds:
                return studentID
#만약 999999까지 다 차면 어떻게 되나요? 
# 에러 처리 하면 됩니다!
# "All available student IDs have been used. A new student ID cannot be generated. Please contact the administrator."
# 이런식으로 message를 띄우고, 시스템 시작 화면으로 돌아가게 하면 될 것 같아요.






#App data setup

#Student data storage, students.data
# /data/students.data 파일을 import 해서 거기에 access해서 json 형태로 저장, 조회해야해요.
class Databsase:
    def __init__(self, dataFile=None):
        self.database = Path(dataFile or Path(__file__).with_name("students.data"))
        try:
            with open(self.dataFile, "r", encoding="utf-8") as file:
                pass
        except FileNotFoundError:
            self.saveStudents([])

    def saveStudents(self, students):
        records = [student.toRecord() for student in students]
        with self.dataFile.open("w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)
        tempFile.replace(self.dataFile)

    def readStudents(self):
        with self.dataFile.open("r", encoding = "utf-8") as file:
            records = json.load(file)
        return [Student.fromRecord(record) for record in records]





#student login 

def loginStudent(self):
        print("\n Welcome to the Student Login System")




