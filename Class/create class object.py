
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Masum", 26)
print(p1.name)
print(p1.age)

class Me:
    def __init__(self, name, age):
        self.n = name
        self.a = age

    def myfunct(self):
        print("Hello my name is " +self.n)

p1 = Me("Billah", 25)
p1.myfunct()
print(p1.n)
print(p1.a)

# Use the words mysillyobject and abc instead of self
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)

del p1.age
del p1
p1.age = 40
print(p1.age)
