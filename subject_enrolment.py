from change_password import changePassword

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
#enrolment 작업하실때 확인 해줏ㅔ요 => 과제 descriptption 에 change password가enrolmentSystem에 포함되어 있어서 선택지를 여기에 넣었지만 function은 다른 파일로 뺄까요?!  
# actioned. changePassword import "from change_password import changePassword"






#  #Subject remove: How should it work. -> enter the subject ID->system find the subject -> remove from the list -> update -> display 