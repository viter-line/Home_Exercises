# # Exercise 7: Print the following pattern

# Write a Python program to print the reverse number pattern using a for loop.

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

n = 5

for x in range(n, 0, -1):
    for y in range(x):
        print(y, end="\n")