x = int(input("Enter the value: "))

mylist = [0, 5, 4, -6, 2, 7, 13, 3, 1]

pairs = 0

print(f"The pairs that sum to {x} are")
for i in range(len(mylist)):
    for j in range(i + 1, len(mylist)):
        if mylist[i] + mylist[j] == x:
            print(f"{mylist[i]} {mylist[j]}")
            pairs += 1
print(f"{pairs} pairs sum to {x}")
