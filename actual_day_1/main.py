# Integers
integer1 = 1
integer2 = 0
integer3 = -1

# Floats
float1 = 1.5

# Strings
string1 = "Hi mom"
string2 = "H"
string3 = "10"  # This is still a string eventhough its a number. The double quotes make it a string
string4 = '10'  # This is still a string eventhough its single quotes

# Booleans
boolean1 = True
boolean2 = False

# Declaring a variable
my_var = 5

# First Method of putting variables into print statements
print("The value is", my_var)
# Second method using f strings
print(f"The value is {my_var} but really my favourite number is {9 + 10}")

# How to get user input
answer = input("Please enter your favourite number: ")
print(type(answer))

answer2 = int(input("Please enter your favourite number again: "))
print(type(answer2))

# int -> integer, int() -> a function to convert other types (strings) to integers
# Since answer is saved as a string when you use * (multiply) it will return a string x amount of times
print(answer * 4)
# Since answer is saved as an int when you use * (multiply) it will do normal multiplication
print(answer2 * 4)
