# 16. Python Match
# For a number from 1 to 3, print "One", "Two", or "Three".

n = int(input())
match n:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
