from student import Student
from database import Database

import random #student ID generation
import re #email and password validation

class UniApp:
#setting the database, initiation. 
    def __init__(self,dataFile=None):
        self.database = Database() if dataFile is None else Database(dataFile)  
        self.students = self.database.loadStudents()
    
#University System requiremnt, choosing the subsystem class. 
    def universitySystem(self):
        while True:
            print("\nWelcome to the University System. please choose a following option")

            print(" (A) Admin")
            print(" (S) Student")
            print(" (X) Exit")
            choice = input("Enter your choice (A-S-X): ").upper()

            if choice == 'A': 
                print("Please login as an admin, otherwise Please choose a different option.")
            elif choice == 'S':
                self.studentSystem()
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
            choice = input("Enter your choice (l-r-x): ").lower()
            if choice == 'l':
                self.loginStudent()
            elif choice == 'r':
                self.registerStudent()
            elif choice == 'x':
                print("Exiting the Student System.")
                break
            else:
                print("Invalid. Please try again.")

# 각각의 기능을 다른 파일로 빼서, 그 student, admin system에서 각각의 def를 선택시에 불러오는 방향으로 파일을 분리하는게 좋을 것 같습니다. 
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
            email = input("Enter your email, following the format (firstname.lastname@university.com): ")  # Todo: firstname.lastname@university.com
            if self.validateEmail(email):
                break
            else:
                print("""Wrong access. Enter a valid email address
                firstname.lastname@university.com""")

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

        studentId = self.generateStudentId()
        if studentId is None: 
            return 
##
        student = Student(name, email, password, studentId)
        newStudents = self.students+[student]

        self.database.saveStudent(newStudents)
        self.students = newStudents

        print("""Registration successful!, 
        please back to the student system and login with your email and password.""")
        print(f"Your student ID is: {student.studentId}")

     
#validation for email and password format
    def validateEmail(self, email): #email  # Todo: email format: firstname.lastname@university.com  # 현재 특수문자 입력이 허용돼서 아이디 부분 "문자.문자" 형식만 입력 가능하도록 validation 수정 => actioned! 
        pattern = r"[A-Za-z]+\.[A-Za-z]+@university\.com"
        return bool(re.fullmatch(pattern, email))

    def validatePassword(self, password): #password  # Todo: password format이 현재는 대문자 + 영문4글자 + 숫자3자리로 고정되어있는데, 대문자 시작 부분만 고정하고 뒤에는 영문, 숫자 입력 순서 상관없이 가능하도록 수정 필요 => actioned! 
        pattern = r"[A-Z][A-Za-z0-9]*"
        return (
            bool(re.fullmatch(pattern,password))
            and sum(c.isalpha() for c in password) >= 5
            and sum(c.isdigit() for c in password) >= 3
            )
    
    
#Auto-student ID generation 
    def generateStudentId(self):
        existingIds = {student.studentId for student in self.students}
        while True: 
            studentID = str(random.randint(1, 999999)).zfill(6)
            if studentID not in existingIds:
                return studentID
#만약 999999까지 다 차면 어떻게 되나요? 
# 에러 처리 하면 됩니다!
# "All available student IDs have been used. A new student ID cannot be generated. Please contact the administrator."
# 이런식으로 message를 띄우고, 시스템 시작 화면으로 돌아가게 하면 될 것 같아요.
        if len(existingIds) > 999999: 
            print ("""
            All available student IDs have been used
            A new student ID cannot be generated.
            Please contact the administrator""")
# if len();  used for execute code based on the number of items in a collection

    def loginStudent(self):
        print("\nwelcome to the Student Login system")
        






        