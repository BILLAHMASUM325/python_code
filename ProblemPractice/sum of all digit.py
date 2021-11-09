number = input("enter value: ")
sum_of_digits = 0
for digits in str(number):
    sum_of_digits += int(digits)
print(sum_of_digits)

num = str(input("Enter the number: "))
result = 0

while num > 0:
    digit = num % 10
    result = result + digit
    num = num // 10
    break
print("Sum is: ", result)