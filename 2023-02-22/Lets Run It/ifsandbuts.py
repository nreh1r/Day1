alist = [52, 4, -1, 17, 81, -2, 75, 24]

base = 14
tracker = 0
has_found_value = False

for i in range(len(alist)):
    if alist[i] < base and alist[i] > tracker and has_found_value:
        tracker = alist[i]
    elif alist[i] < base and not has_found_value:
        tracker = alist[i]
        has_found_value = True
print(tracker)
