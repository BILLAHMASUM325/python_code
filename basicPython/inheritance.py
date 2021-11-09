class Person:
    def __init__(self, fname, lname):
     self.firstname = fname
     self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    pass
x = Student("Masum", "Billah")
x.printname()

class p:
    def __init__(self, name, gender):
        self.fname = name
        self.gen = gender
    def x(self):
        print(self.fname, self.gen)

y = p("Masum", "Male")
y.x()