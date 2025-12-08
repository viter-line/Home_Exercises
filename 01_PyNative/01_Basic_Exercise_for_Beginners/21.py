sentensec = input("Enter a sentence: ")

for i in sentensec:
    if i.isdigit():
        break
print(f"Entered a string: {sentensec}")
print("The string contains at least one digit.")
    # else:
    #     print(f"Entered a string: {sentensec}")
    #     print("The string does not contain any digits.")