sumList = [2, -1, 4, 17]

# Probably not necessary
if len(sumList) == 0:
    sumNums = None


for i in range(len(sumList)):
    if i == 0:
        sumNums = sumList[0]
    else:
        sumNums += sumList[i]

print(f"The sum of your numbers is {sumNums}")
