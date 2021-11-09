mylist = ["Apple", "Apple", "Banana", "Candy", "Cat"]
mylist = list(dict.fromkeys(mylist))
print(mylist)

def myfunction(x):
    return list(dict.fromkeys(x))
mylist = myfunction(["a","b","c","d","e","a","b"])
print(mylist)