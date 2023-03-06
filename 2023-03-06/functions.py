
def say_hi(name):
    print(f"Hello {name}")


say_hi("Jeff")


def add_nums(a, b, c):
    sum_nums = a + b + c
    return sum_nums


a = 1
b = 2
c = 3

print(add_nums(a, b, c))
# 1 -> a = 1
# 2 -> b = 2
# 3 -> c = 3
sum_of_numbers = add_nums(1, 2, 3)

string1 = "hello"
string2 = "hi"

if len(string1) < len(string2):
    for i in range(len(string1)):
        print(f"{string1[i]} {string2[i]}")
else:
    for i in range(len(string2)):
        print(f"second code block")
        print(f"{string1[i]} {string2[i]}")


def line(char, nbr):
    new_string = ""
    for i in range(nbr):
        new_string += char

    return new_string


another_string = "a" * 5  # -> "a" + "a" + "a" + "a" + "a"

print(line("s", 5))
