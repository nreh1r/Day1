input_string = input("Enter a string: ")
index_list = [2, 4, 15, 0, 7, 4, 3, 5]

for i in range(len(index_list)):
    num = index_list[i]
    if num > len(input_string) - 1:
        print(f"position {num} is too large")
    else:
        print(f"{input_string[num]}")
