import random
from cli.change_password import changePassword
from cli.subject import Subject


#301 - max 4 subjects
def checkEnrolmentLimit(student):
    if len(student.subjects) < 4:
        return True
    return False


#302 - unique 3-digit subject ID (001 ~ 999)
def generateSubjectId(students):
    usedIds = []
    for s in students:
        for subject in s.subjects:
            usedIds.append(subject["id"])

    while True:
        subjectId = str(random.randint(1, 999)).zfill(3)
        if subjectId not in usedIds:
            return subjectId


#300 - enrol in a subject
def enrolSubject(student, students, database):
    if not checkEnrolmentLimit(student):
        print("Students are allowed to enrol in 4 subjects only")
        return

    subject = Subject(generateSubjectId(students))
    student.subjects.append(subject.toRecord())
    database.saveStudent(students)

    print(f"Enrolling in Subject-{subject.subjectId}")
    print(f"You are now enrolled in {len(student.subjects)} out of 4 subjects")


#303 - remove a subject by ID
def removeSubject(student, students, database):
    subjectId = input("Remove Subject by ID: ").strip()

    for subject in student.subjects:
        if subject["id"] == subjectId:
            student.subjects.remove(subject)
            database.saveStudent(students)
            print(f"Dropping Subject-{subjectId}")
            print(f"You are now enrolled in {len(student.subjects)} out of 4 subjects")
            return

    print(f"Subject-{subjectId} is not in your enrolment list")


#304 - show enrolled subjects
def viewEnrolment(student):
    print(f"Showing {len(student.subjects)} subjects")
    for subject in student.subjects:
        print(f"[ Subject::{subject['id']} -- mark = {subject['mark']} -- grade = {subject['grade']} ]")


def subjectEnrolmentSystem(student, students, database):
    while True:
        print(f"\nWelcome to the Subject Enrolment System , {student.name}. Please choose a following option: ")
        print ("(c) change password")
        print( "(e) enrol in a subject")
        print ("(r) remove a subject")
        print ("(s) show enrolled subjects")
        print ("(x) exit")
        choice = input("Enter your choice (c-e-r-s-x): ").lower()

        if choice == 'c':
            changePassword(student, students, database)

        elif choice == 'e':
            enrolSubject(student, students, database)

        elif choice == 'r':
            removeSubject(student, students, database)

        elif choice == 's':
            viewEnrolment(student)

        elif choice == 'x':
            print("Exiting the Subject Enrolment System.")
            break

        else:
            print("Invalid choice. Please try again.")
