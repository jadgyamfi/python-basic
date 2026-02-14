story = ""
lastword = ""
while True:
    word = str(input("Please type in a word: "))
    if word == lastword:
        break
    elif word == "end":
        break
    else:
        story = story + " " + word
    lastword = word

print(story)