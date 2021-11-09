class A:
    def display1(self):
        print("I am inside A class ")
class B(A):
    #display1()
    def display2(self):
        print("I am class B")
class C(B):
    #display1()
    #display2()
    def display3(self):
        print("I am class C")
c = C()
c.display1()
c.display2()
c.display3()


class A:
    def display1(self):
        print("I am inside A class ")
class B(A):
    #display1()
    def display2(self):
        print("I am class B")
class C(B):
    #display1()
    #display2()
    def display3(self):
        super().display1()
        super().display2()
        print("I am class C")
c = C()
c.display3()





