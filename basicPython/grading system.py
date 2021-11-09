marks = int(input("enter your score: "))

def s_grade(grade):
    print(f"you got {grade}")

if marks >= 80:
    s_grade("A+")
elif marks < 80 and marks >= 70:
    s_grade("A")
elif marks < 70 and marks >= 60:
    s_grade("B")
else:
    print("you failed")