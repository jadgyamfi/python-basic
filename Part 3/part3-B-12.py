string = input("Please type in a string: ")
ain = ("a" in string)
ein = ("e" in string)
oin = ("o" in string)
if ain:
    print("a found")
else:
    print("a not found")
if ein:
    print("e found")
else:
    print("e not found")
if oin:
    print("o found")
else:
    print("o not found")