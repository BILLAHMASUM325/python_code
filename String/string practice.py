a = "Hello, World"
print(a.upper())

# repalce string
a = "Hello, World"
print(a.replace("H","J"))

# separate the string
b = a.split(",")
print(b)

# we can not combine string and numbers  but we can combine string and number using format() method
age = 26
txt = "my name is Billah, and I am {}"
print(txt.format(age))

# format() method takes unlimited numbers

quantity = 36
itemo = 24
price = 333
z = "I need {} kg powder. Total items is {} Price of total items is {} taka."
print(z.format(quantity, itemo, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))