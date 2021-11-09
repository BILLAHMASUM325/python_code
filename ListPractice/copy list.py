my = ["Banana", "Candy", "apple", "mango"]
new = list(my)
print(new)

my = ["Banana", "Candy", "apple", "mango"]
new = my.copy()
print(new)

list1 = ["a", "b", "c", "d"]
list2 = [1,2,3,4,5,]
list3 = list1 + list2
print(list3)

# another way to add two lists item/ using append() method
list1 = ["a", "b", "c", "d"]
list2 = [1,2,3,4,5,]
for x in list2:
    list1.append(x)
print(list1)

# or another way to add elements one list to another list using extend() method
list1 = ["a", "b", "c", "d"]
list2 = [1,2,3,4,5,]
list1.extend(list2)
print(list1)

