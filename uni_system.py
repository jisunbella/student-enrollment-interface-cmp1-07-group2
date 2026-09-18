<<<<<<< HEAD

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
=======
class UniApp:
    def run(self):
        while True:
            print("\nPlease choose an option:")
>>>>>>> 8175304eaace07778e72d5f325e522b60deb880c
            print(" (A) Admin")
            print(" (S) Student")
            print(" (X) Exit")
            choice = input("Enter your choice (A-S-X): ")

            if choice == 'A': 
                print("Please login as an admin, otherwise Please choose a different option.")
            elif choice == 'S':
                self.studentSystem ()
            elif choice == 'X':
                print("Exiting the UniApp. Goodbye!")
                break
            else:
                print("Invalid. Please try again.")

<<<<<<< HEAD
#The Student subsystem menu, which includes login and registration functionalities for students.
    def studentSystem(self):
        while True:
            print("\n Welsome to the Student System. please choose a following option:")
=======
    def studentSystem(self):
        while True:
            print("\nStudent System Menu:")
>>>>>>> 8175304eaace07778e72d5f325e522b60deb880c
            print(" (l) login")
            print(" (r) register")
            print(" (x) exit")
            choice = input("Enter your choice (l-r-x): ")

            if choice == 'l':
                self.loginStudent ()
            elif choice == 'r':
                self.registerStudent ()
            elif choice == 'x':
                print("Exiting the Student System.")
                break
            else:
                print("Invalid. Please try again.")

<<<<<<< HEAD

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

        print("""Registration successful!, 
        please back to the student system and login with your email and password.""")
        print(f"Your student ID is: {self.generateStudentId()}")
        
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
            studentID = str(random.randint(100000, 999999)).zfill(6)
            if studentID not in existingIds:
                return studentID
#만약 999999까지 다 차면 어떻게 되나요?






#App data setup

#Student data storage, students.data
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




=======
    def loginStudent(self):
        print("Student login functionality is not ready yet.")
    def registerStudent(self):
        print("Student registration functionality is not ready yet.")
>>>>>>> 8175304eaace07778e72d5f325e522b60deb880c
