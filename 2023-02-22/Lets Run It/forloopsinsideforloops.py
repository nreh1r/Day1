mylist = [0, 5, 4, -6, 2, 7, 13, 3, 1]

# Nested for loops
for i in range(len(mylist)):
    for j in range(i + 1, len(mylist)):
        print(f"{mylist[i]} {mylist[j]}")
        print(f"{mylist[i]} + {mylist[j]} = {mylist[i] + mylist[j]}")
