fh = float(input("Enter Hours: "))
fr = float(input("Enter rate: "))
if fh > 40:
    print("Overtime")
    reg = fh * fr
    otp = (fh - 40.0) * (fr * 0.5)
    print(reg, otp)
    xp = reg + otp
else:
    print("Regular")
    xp = fh * fr
print("Pay", xp)


x = float(input("Enter Hours: "))
y = float(input("Enter rate: "))
if x > 40:
    print("Overtime")
    z = x * y
    a = (x - 40.0) * (y * 0.5)
    b = a + z

else:
    print("Regular")
    z = x * y
print("Pay: ", b)


