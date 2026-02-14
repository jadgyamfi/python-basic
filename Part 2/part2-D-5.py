attempts = 1
while True:
    pins = int(input("PIN: "))
    if pins == 4321:
        print("Correct! It took you,", attempts, "attempts")
        break
    else:
        print("Wrong")
        attempts +=1