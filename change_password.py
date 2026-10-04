from registration import validatePassword

def changePassword(student, students, database):
    print("\nWelcome to the Change Password System. Please enter your new password: ")

    while True:
        newPassword = input("Enter your new password: ")

        if not validatePassword(newPassword):
            print("""Wrong access. Please follow the password format.
            Password required
            - Must start with an Uppercase Letter
            - Contain at least 5-letter
            - Contain at least 3-digit Please try again.""")
            continue

        confirmPassword = input("Confirm your new password: ")
        if newPassword != confirmPassword:
            print("Passwords do not match. Please try again.")
            continue

        student.password = newPassword
        database.saveStudent(students) #changed password will be saved in the database

        print ("Password changed successfully! Please use your new password the next time you log in.")
        return  # Exit the function after changing the password

    