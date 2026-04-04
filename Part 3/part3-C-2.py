sent = input("Please type in a sentence: ")
index = 1
print(sent[index - 1])
while index < len(sent):
    index += 1
    if sent[index - 1] == " ":
        print(sent[index])
    
