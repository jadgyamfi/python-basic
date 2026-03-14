word = str(input("Please type in a string: "))
length = len(word)
index = 0
while length > 0:
    length += -1
    print(word[length - 1:])