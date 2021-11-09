def computepay(hours,rate):
    print("In computepay",hours, rate)
sh = input("Enter hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
computepay(fh,fr)

if fh>40:
    reg = fh*fr
    otp = (fh-40.0) * (fr * 0.5)
    xp = reg+otp
else:
    xp = fh*fr
print("Pay: ",xp)

def computepay(hours,rate):
    #print("In computepay", hours,rate)
    if hours>40:
        reg = fh*fr
        otp = (fh-40.0)* (fr*0.5)
        pay = reg+otp
    else:
        pay = fh*fr
    #print("Returning value",pay)
    return pay

fh = float(input("Enter Hours: "))
fr = float(input("Enter Rate: "))
xp = computepay(fh,fr)
print("Pay", xp)