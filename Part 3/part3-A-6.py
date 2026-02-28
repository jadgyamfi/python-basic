limit = int(input("Limit:"))
number = 1
consec = 0
while number < limit:
    consec +=1
    number += (consec + 1)
print(number)
