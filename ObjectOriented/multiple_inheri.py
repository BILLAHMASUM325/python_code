class A:
    def display(self):
        print("I am class A")
class B:
    def display(self):
        print("I am class B")
class C(A,B):
    pass
c1 = C()
c1.display()
