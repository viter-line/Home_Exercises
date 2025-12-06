# Exercise 4: Remove first n characters from a string
# Write a Python code to remove characters from a string from 0 to n and return a new string.
#Note: n must be less than the length of the string.

def remove_chars(words, n):
    x = words[n:]
    return x

print(remove_chars("ПРИВІТТИИИИК",4))
print(remove_chars("trtatatatata",2))
print(remove_chars("123456789",5))

# a = input()
# n = int(input("Enter N: "))
#
# a = list(a)
#
# for i in a[n::]:
#     print(i)