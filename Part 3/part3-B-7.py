string = str(input("Please type in a string: "))
length = len(string)
word = ""
while length > 0:
    word += "-"
    length += -1
print(string)
print(word)
