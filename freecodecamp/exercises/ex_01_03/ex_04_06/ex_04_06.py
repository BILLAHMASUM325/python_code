
def computepay(hours, rate):

    if hours > 40:
        reg = hours*rate
        otp = (hours - 40) * (rate * 0.5)
        print(reg,otp)
        xp = reg + otp

    else:
        xp = hours * rate
    print("Pay:", xp)
computepay(float(input("Enter hours: ")),float(input("Enter Rate: ")))
