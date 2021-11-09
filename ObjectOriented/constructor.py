class Student:
    roll = " "
    gpa = " "

    def __init__(self, roll, gpa): # __init__ is called constructor
        self.roll = roll
        self.gpa = gpa
    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")
karim = Student(101,3.12)
karim.display()

rahim = Student(102,3.24)
rahim.display()