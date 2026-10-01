def subjectEnrolmentSystem(student):
    while True:
        print(f"\nWelcome to the Subject Enrolment System , {student.name}. Please choose a following option: ")
        print ("(c) change password")
        print( "(e) enrol in a subject")
        print ("(r) remove a subject")
        print ("(s) show enrolled subjects")
        print ("(x) exit")
        choice = input("Enter your choice (c-e-r-s-x): ").lower()

        



#enrolment 작업하실때 확인 해줏ㅔ요 
# #Subject remove: How should it work. -> enter the subject ID->system find the subject -> remove from the list -> update -> display 