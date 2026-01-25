# numbers of characters
# https://programming-23.mooc.fi/part-2/1-programming-terminology#programming-exercise-number-of-characters
answer = str(input("Please type in a word: "))
if len(answer) > 1:
    print("There are", len(answer), "letters in the word", answer)
print("Thank you!")