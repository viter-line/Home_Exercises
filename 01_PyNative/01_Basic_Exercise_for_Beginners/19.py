# Exercise: 19: Print Alternate Prime Numbers till 20
# A Prime Number is a number that can only be divided by itself and 1 without remainders (e.g., 2, 3, 5, 7, 11).

for i in range(1, 21):
    if i > 1 and all(i % j != 0 for j in range(2, int(i**0.5) + 1)):
        if i % 2 != 0:
            print(i, end=' ')