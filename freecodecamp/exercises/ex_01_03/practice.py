astr = 'Bob'
try:
    print('Hello')
    istr = int(astr)
    print('There')
except:
    istr = -1
print('Done', istr)

x = int(input("Enter the number: "))
if x < 10:
    print("Small")
elif x < 20:
    print("Medium")
elif x > 20:
    print("Huge")
print(x)