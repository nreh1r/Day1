x = int(input("Enter the value: "))

mylist = [0, 5, 4, -6, 2, 7, 13, 3, 1]

pairs = 0
diff = 0

map = {}

print(f"The pairs that sum to {x} are")
for i in range(len(mylist)):
    diff = x - mylist[i]
    if diff in map:
        print(f"{mylist[i]} {diff}")
        pairs += 1
    else:
        map[mylist[i]] = i
print(f"{pairs} pairs sum to {x}")
