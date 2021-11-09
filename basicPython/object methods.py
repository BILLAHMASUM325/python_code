# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     """method"""
#     def myfunc(self):
#         print("hello my name is:" + self.name)
# """object"""
# p1 = Person("Masum", 26)
# p1.myfunc()

class Person:
  def __init__(mysillyobject, address, name, age):
    mysillyobject.address = address
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my address is " + abc.address)

p1 = Person("Khulna","John", 36)
p1.myfunc()