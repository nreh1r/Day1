print("This program will draw a line for you.")
character = input("Enter a character: ")
length = int(input("Enter the length of the line you want to draw: "))


def draw_line(ch, nbr):
    return ch * nbr


print(draw_line(character, length))
