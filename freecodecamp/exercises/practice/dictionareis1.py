thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "19433"
}
thisdict.update({"Color":"black"})
print(thisdict)
thisdict.pop("model")
print(thisdict)
del thisdict["year"]
print(thisdict)
thisdict.clear()
print(thisdict)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "19433"
}
for x in thisdict:
    print(x)
for x in thisdict:
    print(thisdict[x])
for x in thisdict.keys():
    print(x)
for x,y in thisdict.items():
    print(x,y)

mydict = dict(thisdict)
print(mydict)


# nested dictionaries
myfamily = {
    "child1":{
        "name": "Emil",
        "year": 2004
    },
    "child2":{
        "Name":"Billah",
        "Year": 1994
    },
    "child3":{
        "Name":"MD",
        "Year": 2021
    },
}
print(myfamily)

