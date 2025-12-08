# Exercise 21: Check if a user-entered string contains any digits using a for loop
# Expected Output:

# Enter a string: Pynative123Python
# The string contains at least one digit.

# Enter a string: PYnative
# The string does not contain any digits.

sentensec = input("Enter a sentence: ")

for i in sentensec:
    if i.isdigit():
        break
print(f"Entered a string: {sentensec}")
print("The string contains at least one digit.")
    # else:
    #     print(f"Entered a string: {sentensec}")
    #     print("The string does not contain any digits.")