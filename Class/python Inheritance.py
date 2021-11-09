class Person:
  def __init__(self, fname, lname):
       self.firstname = fname
       self.lastname = lname

  def printname(self):
   print(self.firstname, self.lastname)


x = Person("Mausm","billah")
x.printname()


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

#x = Person("John", "Doe")
x = Person("John", "Doe")
x.printname()

class Age:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
x = Age ('Masum', "Billah")
x.printname()

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)
class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self, fname, lname)
x = Person("Kajol","Aryan")
x.printname()

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self,fname,lname):
        super.__init__(fname,lname)
x = Person("Abida", "Sultana")
x.printname()

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student1(Person):
    def __init__(self,fname,lname):
        super().__init__(fname, lname)
        self.graduationyear = 2020

x = Student1("Apple", "Banana")
print(x.graduationyear)


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
    self.firstname = fname
    self.lastname = lname
x = Student("Mike", "Olsen", 2020)
print(x.graduationyear)
print(x.firstname)
print(x.lastname)

# add a method called welcome to the Student
class Person:
    def __init__(self, fname,lname):
        self.firstname = fname
        self.lastname= lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self, fname, lname, year):
        super.__init__(fname, lname)
        self.graduationyear = year
    def Wellcome(self):
        print("Welcome", self.firstname, self.lastname,"to the class of",self.graduationyear)
x = Person("Don", "007")
x.printname()
