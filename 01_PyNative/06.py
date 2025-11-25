# Exercise 6: Display numbers divisible by 5
# Write a Python code to display numbers from a list divisible by 5

a = input()
a = list(a)
print(type(a))
print(a)
for i in a:
    if (i % 5 == 0):
        print("Displaying numbers divisible by 5:")
