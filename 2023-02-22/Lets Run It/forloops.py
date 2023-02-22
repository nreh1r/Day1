
alist = [52, 4, -1, 17, 81, -2, 75, 24]

# range(start, stop, step)
# range(5) -> 0, 1, 2, 3, 4 and then stop
# range(0, 5, 1) -> 0, 1, 2, 3, 4 and then stop
# stop value is NOT INCLUDED

# range(0, 5, 2) -> 0, 2, 4 and then stop
# range(5, 0, -1) -> 5, 4, 3, 2, 1 and then stop

for i in range(len(alist)):
    print("-----------------------------------------")
    print(f"The value of the index 'i' is {i}")
    print("\n")
    print(f"The current list value is {alist[i]}")
    print("\n")
    print("-----------------------------------------")

# Re written as a while loop

iterator = 0
while iterator < len(alist):
    print("-----------------------------------------")
    print(f"The value of the index 'i' is {iterator}")
    print("\n")
    print(f"The current list value is {alist[iterator]}")
    print("\n")
    print("-----------------------------------------")
    iterator += 1
