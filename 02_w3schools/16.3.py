# 16. Python Match
# Use match to check the type of entered data (str, int, float).

x = input()

match x:
    case a if x.isdigit():
        print("String of digits")
    case a:
        print("String")
