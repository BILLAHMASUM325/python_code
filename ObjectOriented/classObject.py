class Student:
    roll = " "
    gpa = " "
rahim = Student()
rahim.roll = 101
rahim.gpa = 3.10
print(f"Roll: {rahim.roll}, GPA: {rahim.gpa} ")

karim = Student()
karim.roll = 102
karim.gpa = 3.12
print(f"Roll: {karim.roll}, GPA: {karim.gpa}")


class Student:
    roll = " "
    gpa = " "
    def value(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa
    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")

karim = Student()
karim.value(101,3.14)
karim.display()

rahim = Student()
rahim.value(102,3.12)
rahim.display()
