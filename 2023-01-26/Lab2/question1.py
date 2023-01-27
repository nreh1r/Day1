is_running = True
while is_running:
    password = input("Please enter a password: ")
    print("Before if statement")
    print(f"The current value of is_running is {is_running}")
    print(f"The password entered is {password}")
    print("-----------------------------------------")
    if password == "cmput101":
        print("Logging in...")
        is_running = False
    print("After if statement")
    print(f"The current value of is_running is {is_running}")
    print(f"The password entered is {password}")
    print("-----------------------------------------")
