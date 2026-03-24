string = input("Please type in a word: ")
character = input("Please type in a character: ")
length = len(string)
indx = string.find(character)
if (length - 3) >= indx: 
    print(string[indx:indx + 3])