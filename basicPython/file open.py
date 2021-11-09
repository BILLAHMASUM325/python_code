with open("poem.txt", mode="r") as file:
    for line in file.readlines():
        print(line)

with open("poem.txt", mode="r") as document:
    for line in document.readlines():
        print(line)