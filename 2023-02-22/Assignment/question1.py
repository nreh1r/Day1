# Get user input for the base
base = int(input("Enter a base: "))

# Set the list of values to be searched through
alist = [52, 4, -1, 17, 81, -2, 75, 24]

# Set initial values for the current value and index (These current values are arbitrary with how the conditionals are setup)
value = 0
index = 0

# Use this to find if we have found at least one value less than base (This allows our value and index initial values to be arbitrary)
# because the conditionals will be setup to know if we have found a value once or not and so we will know if we are currently have the arbitrary value set or not
has_found_value = False

# Loop through the list (use range so we can keep track of the index position we are currently at)
for i in range(len(alist)):

    # This first condition checks that we already have a current value set in value that isn't the arbitrary value
    # This is because has_found_value must be true
    # It then also checks that the new value is less than base but is also greater than the current (non arbitrary) value of "value"
    if alist[i] < base and alist[i] > value and has_found_value:
        # Set the variable "value" to the new value in the list since it is greater than previous value but less than the base
        value = alist[i]

        # Set the index to the current position so we can keep track of the position the value is in the list
        index = i

    # The elif condition runs to find our first value since it requires has_found_value to be false
    elif alist[i] < base and not has_found_value:
        # Set the variable "value" to the new value in the list since it is greater than previous value but less than the base
        value = alist[i]

        # Set the index to the current position so we can keep track of the position the value is in the list
        index = i

        # Set has_found_value to true so that we now know that we have found a value in the list that is smaller than base
        has_found_value = True

# Check if we have found a value and print out the saved results in "value" and "index"
if has_found_value:
    print(f"{value} at position {index} is the largest value in the list that is smaller than {base}")
# Otherwise print out that there are no values found
else:
    print(f"There are no numbers smaller than {base} in this list")
