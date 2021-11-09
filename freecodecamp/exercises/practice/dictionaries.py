car = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": "1964"
}
x = car.values()
print(x)
car["Year"] = 2020
print(x)
car["Color"] = "White"
print(x)
x = car.items()
print(x)
car["Year"] = 2010
print(x)
if "Year" in car:
    print("Yes, 'modle' is one of keys in the this dict dictionary")
car.update({"Year": 2909})
print(x)
car["New"] = "Yes"
print(x)

purse = dict()
purse ['Money'] = 12
purse ['candy'] = 3
purse['tissues'] = 75
print(purse)

print(purse['candy'])
purse['candy'] = purse['candy']+2
print(purse)

# Comparing Lists and Dictionaries

# List
x = list()
x.append(21)
x.append(143)
print(x)
x[0] = 23
print(x)

# Dictionaries

ddd = dict()
ddd['age'] = 25
ddd['course']= 123
print(ddd)
ddd['age'] = 26
print(ddd)


counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('beau', 0))

# Counting words in Text
counts = dict()
print('Enter a line of text: ')
line = input(' ')
words = line.split()
print('Words:', words)

for word in words:
    counts[word] = counts.get(word,0)+1
print('Counts', counts)



thisdict = {"brand": "Ford", "Model": "mustong", "Year": "1996"}
print(thisdict)

# print the "brand" value of the dictionary
print(thisdict["brand"])
print(len(thisdict))

# get the value of the "model" key
x = thisdict["Model"]
print(x)
x= thisdict.get("Year")
print(x)
y = thisdict.keys()
print(y)

# add a new item by keys

car = {
    "brand": "ford",
    "model":"xesd",
    "year":"1983"
}
x = car.keys()
print(x)
car["color"]= "white"
print(x)
x = car.values()
print(x)