points = int(input("How many points [0-100]: "))
if points < 0:
    grade = "impossible!"
elif points < 50:
    grade = "Fail"
elif points < 60:
    grade = "1"
elif points < 70:
    grade = "2"
elif points < 80:
    grade = "3"
elif points < 90:
    grade = "4"
elif points < 101:
    grade = "5"
else:
    grade = "impossible!"
print("Grade:", grade)
