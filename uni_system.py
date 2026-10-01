
from database import Database
import registration
import login
import subject_enrolment


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

# 각각의 기능을 다른 파일로 빼서,  student, admin system에서 각각의 def를 선택시에 불러오는 방향으로 파일을 분리하는게 좋을 것 같습니다. 
#Student Registration functionality.
    def registerStudent(self):
        self.students = registration.registerStudent(
            self.students,
            self.database
        )

    def loginStudent(self):
        self.students = self.database.loadStudents()
        student = login.loginStudent(self.students)

        if student is None:
            return None
        
        if student is not None:
            subject_enrolment.subjectEnrolmentSystem(student)
            return student

#login 후 student page;' enrolment page로 가게 해야합니다; here need to be connected to the subject enrolment system 





        