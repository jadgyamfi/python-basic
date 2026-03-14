word1 = str(input("Please type in a string : "))
length = len(word1)
second2last = word1[length - 2]
second = word1[1]
if second2last == second:
    print("The second and the second to last characters are", second)
else:
    print("The second and the second to last characters are different")