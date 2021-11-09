weight = int(input('Weight: '))
unit = input('(L)bs or (K)kg: ')
if unit.upper() == "L":
    convert = weight * 0.45
    print(f"you are {convert} kilos")
else:
    convert = weight/0.45
    print(f"You are {convert} pounds")

weight = int(input('Weight: '))
M = input('(L)lbs or (K)kg: ')
if M.upper() =="L":
    convert = M *  0.45
    print(f"You are {convert} kilos")
else:
    convert = M / 0.45
    print(f"Your are {convert} pounds")




