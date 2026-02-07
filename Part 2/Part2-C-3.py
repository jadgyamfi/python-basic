import math
fizz = ""
buzz = ""
number = float(input("Number: "))
if (number / 3 ) == math.floor(number / 3):
    fizz = "Fizz"
if (number / 5) == math.floor(number / 5):
    buzz = "Buzz"
print(fizz + buzz)