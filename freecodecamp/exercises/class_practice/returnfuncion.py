def great(x,y):
    z = x+y
    return z
print (great(2,3), "Glenn")
print(great(1,2), 'Sally')

def get(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
print(get('en'), 'Glen')
print(get('es'), 'Sally')
print(get('fr'), 'Machael')

def computepay(hours, rate):
    print(hours,rate)
fh = float(input("Enter hours: "))
fr = float(input('Enter rate: '))
computepay(fh,fr)
if fh > 40:
    reg = fr * fh
    otp = (fh - 40.0)*(fr*0.5)
    xp = reg+otp
else:
    xp = fh*fr
print("Pay: ",xp)


