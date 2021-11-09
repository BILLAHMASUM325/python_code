num = int(input("Enter the number: "))
for i in range(2, num):
    if num % i == 0:
        print("It's not prime number")
        break
else:
    print("It's prime number")