is_running = True
output_string = ""
while is_running:
    letter = input("Enter a character: ").lower()
    if letter == "z":
        is_running = False
    elif letter == "x":
        continue
    else:
        output_string += letter

print(output_string)
