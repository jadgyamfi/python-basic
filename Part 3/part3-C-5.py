oddeven = "e"
n = int(input("Type a number: "))
i = 0
while i <= n:
    i += 1
    if oddeven == "e":
        print(i + 1)
        print(i)
        oddeven = "o"
        continue
    elif oddeven == "o":
        oddeven = "e"