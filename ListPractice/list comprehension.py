fruits = ["apple", "Banana", "Cherry", "Candy"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x for x in fruits]
print(newlist)

newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    newlist = x.upper()
    print(newlist)

list = ["banana", "cherry", "apple", "paper", "mango"]
list.sort()
print(list)

# sort desending order
list = ["Banana", "Candy", "Apple", "Mango"]
list.sort(reverse=True)
print(list)


list_b= ["Banana", "Candy", "apple", "mango"]
list_b.sort(key = str.lower)
print(list_b)

list_b= ["Banana", "Candy", "apple", "mango"]
list_b.reverse()
print(list_b)



thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)




