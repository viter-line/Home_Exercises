# Exercise 14: Print a downward half-pyramid pattern of stars
# * * * * *  
# * * * *  
# * * *  
# * *  
# *


l = 5
for i in range(l, 0, -1):
    for j in range(0, i):
        print("*", end=" ")
    print()