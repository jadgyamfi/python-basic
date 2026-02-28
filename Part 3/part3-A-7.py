limit = int(input("Limit:"))
number = 1
consec = 0
words = "1"
while number < limit:
    consec +=1
    words += (" + " + str(consec + 1))
    number += (consec + 1)
print(number)
print(words + " = " + str(number))