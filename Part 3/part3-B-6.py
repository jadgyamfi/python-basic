length = int(input("Width: "))
height = int(input("Height: "))
while height > 0:
    word = ""
    lengthcount = length
    while lengthcount > 0:
        word = word + "#"
        lengthcount += -1
    print(word)
