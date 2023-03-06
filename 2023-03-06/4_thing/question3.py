letter = input("Enter a letter: ")
string_input = input("Enter a string: ")


def remove_letter(theLetter, theString):
    new_string = ""
    for i in range(len(theString)):
        if theString[i] != theLetter:
            new_string += theString[i]
    return new_string


print(
    f"The string after removing letter {letter} is {remove_letter(letter, string_input)}")
