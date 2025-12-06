# Exercise 6: Display numbers divisible by 5
# Write a Python code to display numbers from a list divisible by 5

a = [1, 3, 5, 10,23, 15, 20, 43, 50, 60]
for x in a:
    if x % 5 == 0:
        print("Displaying numbers divisible by 5:",x)