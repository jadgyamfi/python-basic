print("Person 1:")
p1 = input("Name: ")
p1age = int(input("Age: "))
print("Person 2L")
p2 = input("Name: ")
p2age = int(input("Age: "))
if p1age > p2age:
    print("The eldest is", p1)
elif p2age > p1age:
    print("The eldest is", p2)
else:
    print(p1, "and", p2, "are the same age")