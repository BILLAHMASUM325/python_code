import re
txt = "The rain is Spain"

x = re.findall("[a-m]", txt)
print(x)

# find all digit characters

text = "the will be 59 characters"
x = re.findall("\d", text)
print(x)

# search a sequence that starts with "he" followed by two (any) characters, and an "o"

text = "hello planet"
x = re.findall("he..o", text)
print(x)

# Ends with characters

text = "Hello Planet"
x = re.findall("Planet$", text)
if x:
    print("Yes, the string ends with 'planet'")
else:
    print("No mater")

# Zero or more occurrences
txt = "hello planet"
x = re.findall("he.*o", txt)
print(x)

