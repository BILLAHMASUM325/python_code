def greate(lang):
    if lang == 'es':
        print("Hola")
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')
greate('en')
greate('es')
greate('fr')

def gret():
    return "Hello"
print(gret(),"Glenn")
print(gret(),"Sally")

def great(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
print(great('en'),'Glenn') # Hello Glenn
print(great('fr'), 'Sally') # Bonjour Sally
print(great('es'), 'Michael') # Hola Michael

def addtwo (a,b):
    added = a+b
    return added
x = addtwo(5,8)
print(x)