# While loops

# while (condition):
#   executes code
# while loop terminates when the condition becomes false

is_less_than = True
# while True is what the bottom code represents
while is_less_than:
    num = int(input("Enter a number greater than 10: "))
    if num > 10:
        print("the number is greater than 10")
        # is_less_than = False
        break
        # Either setting is_less_than = Flase or break will do the same thing here
# while is_less_than and while is_less_than == True are the same thing

# max = int(input())
# continue1 = True
# nbr = 0
# while continue1:
#     print(nbr)
#     nbr += 2
#     if nbr >= max:
#         continue1 = False
