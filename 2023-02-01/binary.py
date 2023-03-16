number_int = 68
number_binary = ""
while number_int:
    remainder = number_int % 2
    number_binary += str(remainder)
    number_int = number_int // 2

right_order = number_binary[::-1]
print(right_order)
