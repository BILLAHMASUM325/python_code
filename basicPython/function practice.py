def n (first, second):
    return first / second

num_1 = int(input("Enter 1st number: "))
num_2 = int(input("Enter 2nd number: "))

div = n(num_1, num_2)

remainder = num_1 % num_2
print(f"Multiplication: {num_1} / {num_2} = {div}")
print(f"Remainder: {num_1} / {num_2} = {remainder}")

