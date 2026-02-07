age = int(input("What is your age? "))
if age >= 5:
    print("Ok, you're", age, "years old")
elif age < 5 and age > 0:
    print("I supspect you can't write yet...")
else:
    print("That must be a mistake")