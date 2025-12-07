# Exercise 16: Check Palindrome Number
# A palindrome number is a number that remains the same when its digits are reversed. In simpler terms, it reads the same forwards and backward. For example 121, 5005.

# Write a code to check if given number is palindrome.

def is_palindrome_number(num):
    # Convert the number to string
    str_num = str(num)
    # Check if the string is equal to its reverse
    return str_num == str_num[::-1]
# Test the function
number = 121
if is_palindrome_number(number):
    print(f"{number} is a palindrome number.")
else:
    print(f"{number} is not a palindrome number.")