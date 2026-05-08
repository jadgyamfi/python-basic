def hash_square(num):
    i = num
    while i > 0:
        word = ""
        v = num
        while v > 0:
            v += -1
            word += "#"
        print(word)
        i += -1
        
hash_square(3)
print("")
hash_square(5)