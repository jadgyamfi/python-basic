word1 = str(input("Please type in the 1st word: "))
word2 = str(input("Please type in the second word: "))
if word1 > word2:
    print(word1, "comes alphabetically last")
elif word2 > word1:
    print(word2, "comes alphabetically last")
else:
    print("You gave the same word twice")