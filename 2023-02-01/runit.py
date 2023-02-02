my_list = [0, 1, 0, 1, 1]
b = 2
val = 1
total = 0

next = len(my_list) - 1
print("b | next | my_list | my_list[next] | val | total")
while next >= 0:
    print(
        f"{b} | {next}    | {my_list} | {my_list[next]}     | {val}   | {total}")
    total = total + (my_list[next] * val)
    val = val * b
    next = next - 1
