modList = [0, 4, 2, -2, -8, 0, 5, 19, 200, -3]
numZeros = 0
for i in range(len(modList)):

    if modList[i] == 0:
        numZeros += 1
    elif modList[i] < 0:
        modList[i] = 0

print(f"There were {numZeros} zeroes in the original list")
print(f"The new list is {modList}")
