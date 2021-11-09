def myfun(*kid):
    print("The youngest child is " +kid[2])
myfun("Email","Tobius" , "Linus")

def x(cl3, cl2, cl1):
    print("The youngest child is " + cl3)
x(cl1 = "Email", cl2 = "Tobias", cl3 = "Linus")

def myfun(**kid):
    print("His name is " + kid["lname"])
myfun(fname = "Tobias", lname = "Refesnes")

def myf(country = "Norway"):
    print("I am from " + country)
myf("Sweden")
myf("Bangladesh")
myf()
myf("Canada")

def myfunct(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "candy"]
myfunct(fruits)
