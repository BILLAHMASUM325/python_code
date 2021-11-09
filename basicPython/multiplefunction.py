def two_number_multiple(first, second):
    return first * second

num_1 = int(input("Enter 1st number: "))
num_2 = int(input("Enter 2nd number: "))
multi = two_number_multiple(num_1, num_2)
print(f"{num_1}+ {num_2} = {multi}")