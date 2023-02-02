numList = [2, 4, 5, 6, 7]
squareList = []

for i in range(len(numList)):
    num = numList[i]
    # squareList.append(num ** 2)
    squareList = squareList + [num * num]

print(f"The squares of your numbers are: {squareList}")
