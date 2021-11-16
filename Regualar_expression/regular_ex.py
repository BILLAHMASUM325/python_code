import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("Yes! We have a match")
else:
    print("No match")

text = "This is my laptop. Today I bought a ear phone"

x = re.search("^This.*phone", text)

if x:
    print("Yes! we have a match")
else:
    print("No mater")