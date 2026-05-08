while True:
    num = int(input("Please type in a number:"))
    ind = 0
    fact = 1
    while ind < num:
        ind += 1
        fact *= ind
    print("The factorial of the number", num, "is", fact)