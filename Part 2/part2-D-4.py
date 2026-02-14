password = str(input("Password: "))
while True:
    reentered = str(input("Repeat password: "))
    if reentered == password:
        print("User account Created:")
        break
    else:
        print("They do not match!")