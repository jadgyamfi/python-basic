value = float(input("Value of gift: "))
if 5000 > value:
    tax = "No tax!"
elif value < 25000:
    tax = 100 + ((value - 5000) * 0.08)
elif value < 55000:
    tax = 1700 + ((value - 25000) * 0.1)
elif value < 200000:
    tax = 4700 + ((value - 55000) * 0.12)
elif value < 1000000:
    tax = 22100 + ((value - 200000) * 0.15)
else:
    tax = 142100 + ((value - 1000000) * 0.17)
if tax == "No tax!":
    print(tax)
else:
    print("Amount of tax:", tax, "euros")