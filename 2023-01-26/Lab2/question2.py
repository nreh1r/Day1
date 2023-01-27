fruit = input("Enter a fruit: ").lower()
# Using an if statement
# Formatted for proper english
# if fruit == "apple":
#     print(f"We grow {fruit}s")
# elif fruit == "pear":
#     print(f"We grow {fruit}s")
# elif fruit == "berry":
#     print(f"We grow {fruit[0:4]}ies")
# else:
#     print(f"We don't grow this fruit")

# Answering the question properly
if fruit == "apple":
    print(f"We grow {fruit}")
elif fruit == "pear":
    print(f"We grow {fruit}")
elif fruit == "berry":
    print(f"We grow {fruit}")
else:
    print(f"We don't grow this fruit!")

# More concise version
fruits = ["apple", "pear", "berry", "tomato", "tangerine"]
if fruit in fruits:
    print(f"We grow {fruit}")
else:
    print("We don't grow this fruit")
