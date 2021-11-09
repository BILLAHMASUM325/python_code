def myfunction():
    global x
    x = "awesome"
myfunction()
print("Python is " + x)

def myfunc():
    global x
    x = "Fantastic"

myfunc()
print("Python is " + x)

## Change global keyword

x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)