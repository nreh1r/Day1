# Tracing b)
x = 6
y = 0
z = 2
while x > y:
    x -= 1
    if y < 2:
        y += 1
        z += x
print(x, y, z)

# Tracing c)
x = 6
y = 0
z = 2
if x > y:
    x -= 1
    while y < 2:
        y += 1
        z += x
print(x, y, z)
