# 16. Python Match
# Create a variable day = "Monday" and use match to print the day of the week.

day = "Monday"
match day:
    case "Monday":
        print("Monday")
    case _:
        print("Other day")
