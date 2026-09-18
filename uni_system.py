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
            choice = input("Enter your choice (A-S-X): ")

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
            choice = input("Enter your choice (l-r-x): ")

            if choice == 'l':
                self.loginStudent()
            elif choice == 'r':
                self.registerStudent()
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
            email = input("Enter your email (name@university.com): ")
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
    def validateEmail(self, email): #email
        pattern = r"[^@\s]+@university\.com"
        return bool(re.fullmatch(pattern, email))

    def validatePassword(self, password): #password
        pattern = r"[A-Z][A-Za-z]{4,}[0-9]{3,}"
        return bool(re.fullmatch(pattern, password))
    
#Auto-student ID generation 
    def generateStudentId(self):
        existingIds = {student.studentId for student in self.students}
        while True: 
            studentID = str(random.randint(1, 999999)).zfill(6)
            if studentID not in existingIds:
                return studentID

#student login 
    def loginStudent(self):
        print("\n Welcome to the Student Login System, not ready yet")