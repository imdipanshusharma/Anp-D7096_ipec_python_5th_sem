class Student:

    def __init__(self):
        self.student_id = 0
        self.name = ""
        self.course = ""
        self.marks = 0

    def accept_data(self):
        self.student_id = int(input("Enter Student ID: "))
        self.name = input("Enter Name: ")
        self.course = input("Enter Course: ")
        self.marks = int(input("Enter Marks: "))

    def display_data(self):
        print("\n------ Student Details ------")
        print("Student ID :", self.student_id)
        print("Name :", self.name)
        print("Course :", self.course)
        print("Marks :", self.marks)

    def check_result(self):
        if self.marks >= 35:
            print("Result : Pass")
        else:
            print("Result : Fail")


# Object creation
s1 = Student()

s1.accept_data()
s1.display_data()
s1.check_result()