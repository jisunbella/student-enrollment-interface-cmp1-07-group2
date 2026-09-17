class UniApp:
    def run(self):
        while True:
            print("\nPlease choose an option:")
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

    def studentSystem(self):
        while True:
            print("\nStudent System Menu:")
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

    def loginStudent(self):
        print("Student login functionality is not ready yet.")
    def registerStudent(self):
        print("Student registration functionality is not ready yet.")