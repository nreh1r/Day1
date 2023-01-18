# Question 1
print("Hello World")

# # Question 2
num = int(input("Enter a number larger than 10: "))

amount = 11 - num
if num > 10:
    print(f"{num} is correct")
    print(num, "is correct")
elif num < 10:
    print(f"{num} is too small by at least {10 - num + 1}")
    print(num, "is too small by at least", amount)
# else:
#     print("num is equal to ten")
print("Done")

# functions
# function are called by their name and then parentheses
# eg. print()
# inside the parentheses is where you pass your arguments to the function
# eg. print("Hello World")

# Question 3

is_less_than = True
while is_less_than:
    new_num = int(input("Enter a number greater than 10: "))
    if new_num > 10:
        print(f"{new_num} is valid")
        is_less_than = False
    elif new_num < 10:
        print(f"{new_num} is too small by at least {11 - new_num}")
    else:
        print(f"{new_num} is not greater than 10")
print("Done")
