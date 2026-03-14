string = str(input("Please type in a string: "))
length = 20 - len(string)
word = ""
while length > 0:
    word += "*"
    length += -1
print(word + string)
