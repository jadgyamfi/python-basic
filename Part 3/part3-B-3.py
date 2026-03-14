word = str(input("Please type in a string: "))
wordlength = len(word)
while wordlength > 0:
    print(word[wordlength - 1])
    wordlength += -1