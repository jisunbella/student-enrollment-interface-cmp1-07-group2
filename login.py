#exit page; go back to the before page; atm, don't have to have 
#def  exitOrLogin(string)
 #   value = input(string)
#
 #   if value.string() == "X":
  #      print ("Returning to the student system.")
   #     return None
    #return value 


def loginStudent(students):
    print("\nwelcome to the Student Login system.")
    print ("""please login with your validated email and password
    """)

    while True:
        email = input("Enter your registered email: ")
        password = input ("enter you password: ")

        for student in students:
            if student.email == email and student.password == password:
                print ("login successful!, Welcome!")
                return student 

        print ("Login failed. please check your email and password.")
        print ("please try again")
        print ("if you have not registered, exit and register first.")
        
