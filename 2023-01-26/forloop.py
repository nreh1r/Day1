string1 = "nick"
string2 = "nicole"

for char in string1:
    # ^ char = string1[i] over and over as i goes from 0 to 3
    print(char)

matches = 0

for i in range(len(string1)):
    print(i)
    print(string1[i])
    if string1[i] == string2[i]:
        matches += 1
        # matches = matches + 1
        # i += 1
