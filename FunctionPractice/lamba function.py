
x = lambda a: a+10
print(x(5))

x = lambda a,b: a*b
print(x(5,6))

x = lambda a,b,c: a+b+c
print(x(2,3,4))

def myfun(n):
    return lambda a: a * n
mydoubler = myfun(2)
print(mydoubler(11))

def myf(n):
    return lambda a:a*n
myd = myf(2)
myt = myf(3)
print(myd(11))
print(myt(11))