# # Exercise 8: Print the following pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for x in range(10):
    for y in range(x):
        print(x, end="")
    print("\n")