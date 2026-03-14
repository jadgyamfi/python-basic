string = str(input("Please type in a string: "))
multiplier = int(input("Please type in an anmount"))
times = multiplier
fullstring = ""
while times > 0:
    fullstring = fullstring + string
    times += -1
print(fullstring)