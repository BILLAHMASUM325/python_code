def num (n):
    if n % 2 == 0:
        return True
    else:
        return False

even = []
new = 0
user = int(input("Limit: "))
while new < user:
     if num(new):
         even.append(new)
     new =  new + 1
print(f"Even numbers: {even}")
print("Finished")

