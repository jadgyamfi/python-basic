string = str(input("Word: "))
length = len(string)
freedigits = 28 - length
wordsleft = int((freedigits - length) / 2)
wordsright = freedigits - wordsleft - length
print(30*"*")
print("*" + (wordsleft * " ")+(string)+(wordsright * " ") + "*")
print(30*"*")