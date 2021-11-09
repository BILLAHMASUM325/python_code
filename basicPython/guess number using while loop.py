secret_number = 10
g_count = 0
guess_limit = 5

while g_count < guess_limit:
    guess = int(input("Guess: "))
    if guess == secret_number:
        print("You won: ")
        break
else:
    print('You failed')