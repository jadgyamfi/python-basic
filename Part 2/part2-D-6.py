year = int(input("Year: "))
lpyear = year
while True:
    lpyear +=1 
    div4 = 0 == lpyear % 4
    div100 = 0 == lpyear % 100
    div400 = 0 == lpyear % 400
    if div400:
        break
    elif div4 and not div100:
        break
print("The next leap year is", lpyear)