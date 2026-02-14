while True:
    num = float(input("Please type in a number:"))
    if num == 0:
        print("Exiting...")
        break
    if int(num) == num:
        print(num)
    else:
        print("Invalid number")