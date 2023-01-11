# if else statement
# num2 = 2
# num_to_string = str(num2)
# print(num_to_string)
# print(type(num_to_string)) -> type() will return if the variable is an int, string, boolean, float, ...

# > -> greater than
# < -> less than
# == -> equal to (the double equal sign matters it checks equality whereas = is assignment)
# >= -> greater than or equal to
# <= -> less than or equal to
# != -> not equal

# is_running = True
# while is_running:
#     num = int(input("Please enter a number: "))
#     if num >= 10:
#         # Codeblock 1
#         print("You can buy lunch.")
#         print("Congrats on no longer being a peasant")
#         is_running = False
#     else:
#         # Codeblock 2
#         print("Sorry you're broke :)")
# print("-----------------------------------")

color = input("What is your favourite colour on a traffic light? ").lower()
# print(color)

# If color = "rEd"
# .lower() converts color to red
# .upper() converts color to RED
# .title() converts color to Red

if color == "green":
    print("You like to go fast!")
elif color == "yellow":
    print("You like slowing down.")
elif color == "red":
    print("You like stopping.")
else:
    print("You don't know colours")

# This will not work the same way the above if statement does the else is always tied to the closest if above it
# if color == "green":
#     print("You like to go fast!")
# elif color == "yellow":
#     print("You like slowing down.")
# elif color == "red":
#     print("You like stopping.")
# else:
#     print("You don't know colours")
