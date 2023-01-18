# use a while loop to continually ask for a number from the user
# while int(input("enter a number")):
#     print("Done")

# while True:
#     print("DOne")

# while 5: -> this will run forever because 5 is truthy
# while 0: -> this will never run because 0 is falsy

a = "activation"
b = "t"
i = 0
flag = True
answer_string = ""
print("| a          | b | flag  | i | a[i] |")
# print("____________________________________")
while i < len(a):
    if a[i] == b:
        flag = not flag
    print(f"| {a} | {b} | {flag and f'{flag} '} | {i} |   {a[i]}  |")
    if flag:
        # print(f"output: {a[i]}")
        answer_string += a[i]
    i += 1

print("Answer output:")
for char in answer_string:
    print(char)
