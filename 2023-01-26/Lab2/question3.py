string1 = input("Enter string 1:")
string2 = input("Enter string 2:")

counter = 0

if len(string1) < len(string2):
    for i in range(len(string1)):
        if string1[i] == string2[i]:
            counter += 1
else:
    for i in range(len(string2)):
        if string1[i] == string2[i]:
            counter += 1

print(f"The strings matched {counter} times.")

# Get two different strings from the user
# Checked for the smaller string
# Loop through the smaller string and match characters
