# fix the syntax 
# https://programming-23.mooc.fi/part-2/1-programming-terminology#programming-exercise-fix-the-syntax
number = int(input("Please type in a number: "))
if number > 100:
    print("The number was greater than 100")
    number = number - 100
    print("Now its value has decreased by one hundred")
    number = str(number)
    print("Its value is now " + number)
number = str(number)
print(number + " must be my lucky number!")
print("Have a nice day")