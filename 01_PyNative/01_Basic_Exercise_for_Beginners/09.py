# Exercise 9: Check Palindrome Number
# Write a Python code to check if the given number is a palindrome.
# A palindrome number reads the same forwards and backward. For example, 545 is a palindrome number.
#

a = list(input("Enter your number, please: "))
b = reversed(a)
print(a)
print(b)
if a == reversed(a):
    print("original number", a)
    print("Yes. given number is palindrome number")
else:
    print("original number", a)
    print("No. given number is not palindrome number")