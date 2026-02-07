year = int(input("Please type in a year: "))
div4 = 0 == year % 4
div100 = 0 == year % 100
div400 = 0 == year % 400
if div4 and not div100:
    print("That year is a leap year.")
elif div400:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")

