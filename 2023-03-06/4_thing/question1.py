def square(n):
    return n ** 2


input_num = int(input("Enter the number: "))

sum_of_squares = 0

for i in range(1, input_num + 1):
    sum_of_squares += square(i)

print(sum_of_squares)
