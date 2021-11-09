grocery = ["Apple", "Banana", "Onion", "Tomato"]
for item in grocery:
    if item == "Onion":
        break
    print(item)

grocery_1 = ["Onion", "ginger", "potato", "cucumber"]

for item_1 in grocery_1:
    if item_1 == "potato":
        break
    print(item_1)

grocery_2 = ["Mango", "strawberry", "cucumber"]

for item_2 in grocery_2:
    if item_2 == "cucumber":
        break
    print(item_2)

for item in ['Masum', 'Abida', 'Maijur Billah']:
    print(item)

for item in ['1','2','3','4','5']:
    print(item)

"""it boring we use function after in """
for item in range(10):
    print(item)
"""here is output 0 so I don't need 0 in output"""
for item in range(2, 9):
    print(item)

prices = [10, 20, 30]
total = 0

for price in prices:
    total = total + price
print(f"Total: {total}")

secret = 9
guess = 0
limit = 3

while guess <= limit:
    gue = int(input("Enter guess number: "))
    if gue == secret:
     print("You won")
    break
else:
    print('you failed')

for name in ['masum', 'billah', 'abida', 'renesa']:
    print(name)
