import tkinter as tk
from tkinter import messagebox 

from gui.change_password_gui import changePasswordGUI
from cli.subject_enrolment import checkEnrolmentLimit, generateSubjectId
from cli.subject import Subject

class subjectEnrolmentGUI:
    def __init__(self, root, app, student):
        self.root = root
        self.app = app
        self.student = student

    def enrolmentWindow(self):
        self.enrolTitle = tk.Label (
            self.root,
            text = "This is Subject Enrolment System",
            **self.app.titleStyle
        )
        self.enrolTitle.pack(
            pady = self.app.titlePadding
        )

        self.enrolSubTitle = tk.Label(
            self.root,
            text = f"Welcome, {self.student.name} ({self.student.studentId}) Please choose a following option",
            **self.app.subTitleStyle
        )
        self.enrolSubTitle.pack(
            pady=self.app.subTitlePadding
        )

#enrolment system label 
        panel = self.app.createMenuPanel()
        self.changePasswordButton = self.app.createMenuButton(panel, "Change the Password", self.changePassword)
        self.enrolSubjectButton = self.app.createMenuButton(panel, "Enrol in a subject", self.enrolSubject)
        self.removeSubjectButton = self.app.createMenuButton(panel,"Remove a subject",self.removeSubjectWindow)
        self.viewEnrolmentButton = self.app.createMenuButton(panel,"view enrolment", self.viewEnrolmentWindow)
        self.logoutButton = self.app.createMenuButton(panel, "logout", self.app.mainMenu, self.logout )



    def changePassword(self):
        self.app.clearWindow()

        changePassword = changePasswordGUI(
            self.root, 
            self.app,
            self.student
        )
        changePassword.changePasswordWindow()

#300 - enrol in a subject (max 4)
    def enrolSubject(self):
        if not checkEnrolmentLimit(self.student):
            messagebox.showerror(
                "Enrolment Limit",
                "Students are allowed to enrol in 4 subjects only"
            )
            return

        subject = Subject(generateSubjectId(self.app.students))
        self.student.subjects.append(subject.toRecord())
        self.app.database.saveStudent(self.app.students)

        messagebox.showinfo(
            "Enrolment Successful",
            f"Enrolling in Subject-{subject.subjectId}\n"
            f"You are now enrolled in {len(self.student.subjects)} out of 4 subjects"
        )

#304 - show enrolled subjects
    def viewEnrolmentWindow(self):
        self.app.clearWindow()

        self.viewTitle = tk.Label(
            self.root,
            text = f"Showing {len(self.student.subjects)} subjects",
            **self.app.titleStyle
        )
        self.viewTitle.pack(pady = self.app.titlePadding)

        self.showSubjectList()

        self.exitButton = self.app.createFormButton(
            self.root,
            "Back",
            self.backToEnrolment,
            isBack=True
        )

#303 - remove a subject by ID
    def removeSubjectWindow(self):
        self.app.clearWindow()

        self.removeTitle = tk.Label(
            self.root,
            text = "Remove a subject",
            **self.app.titleStyle
        )
        self.removeTitle.pack(pady = self.app.titlePadding)

        self.showSubjectList()

        self.subjectIdLabel = tk.Label(
            self.root,
            text="Subject ID",
            **self.app.formLabelStyle
        )
        self.subjectIdLabel.pack(pady=(5, 5))

        self.subjectIdEntry = tk.Entry(
            self.root,
            **self.app.formEntryStyle
        )
        self.subjectIdEntry.pack(pady=(0, 10))

        self.removeButton = self.app.createFormButton(
            self.root,
            "Remove",
            self.removeSubject
        )

        self.exitButton = self.app.createFormButton(
            self.root,
            "Back",
            self.backToEnrolment,
            isBack=True
        )

    def removeSubject(self):
        subjectId = self.subjectIdEntry.get().strip()

        for subject in self.student.subjects:
            if subject["id"] == subjectId:
                self.student.subjects.remove(subject)
                self.app.database.saveStudent(self.app.students)
                messagebox.showinfo(
                    "Subject Removed",
                    f"Dropping Subject-{subjectId}\n"
                    f"You are now enrolled in {len(self.student.subjects)} out of 4 subjects"
                )
                self.removeSubjectWindow() #refresh the list
                return

        messagebox.showerror(
            "Subject Not Found",
            f"Subject-{subjectId} is not in your enrolment list"
        )
        self.subjectIdEntry.delete(0, tk.END) #clear the entry

#subject list (view, remove 화면에서 같이 사용)
    def showSubjectList(self):
        panel = self.app.createMenuPanel()

        if len(self.student.subjects) == 0:
            text = "You are not enrolled in any subjects yet."
        else:
            text = ""
            for subject in self.student.subjects:
                text += f"[ Subject::{subject['id']} -- mark = {subject['mark']} -- grade = {subject['grade']} ]\n"

        self.subjectListLabel = tk.Label(
            panel,
            text=text.strip(),
            justify="left",
            **self.app.formLabelStyle
        )
        self.subjectListLabel.pack()

    def backToEnrolment(self):
        self.app.subjectEnrolmentPage(self.student)

    def logout(self):
        self.app.currentStudent = None
        self.app.studentMenu()