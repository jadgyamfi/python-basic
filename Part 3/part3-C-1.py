number = int(input("Please type in a number: "))
multi1 = 1
while multi1 <= number:
    multi2 = 1
    while multi2 <= number:
        print(multi1, "x", multi2, "=", (multi1*multi2) )
        multi2 += 1
    multi1 += 1