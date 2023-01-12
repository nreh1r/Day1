
num = int(input("Enter a number: "))
if num < 10:
    print(num, "is less than 10")
elif num < 20:
    print(num, "is between 10 and 19")
elif num < 50:
    print(num, "is between 20 and 49")
else:
    print(num, "is greater than 50")
