try:
    fh = float(input("Enter Hours: "))
    fr = float(input("Enter rate: "))
except:
    print("Error, Enter numeric value")

if fh > 40:
    print("Overtime")
    reg = fh * fr
    otp = (fh - 40.0) * (fr * 0.5)
    print(reg, otp)
    xp = reg + otp
else:
    xp = fh * fr
print("Pay", xp)

try:

    x = float(input("Enter Hours: "))
    y = float(input("Enter rate: "))
except:
    print("Error, Enter nummeric value. ")

if x > 40:
    print("Overtime")
    z = x * y
    a = (x - 40.0) * (y * 0.5)
    b = a + z

else:
    print("Regular")
    z = x * y
print("Pay: ", b)

