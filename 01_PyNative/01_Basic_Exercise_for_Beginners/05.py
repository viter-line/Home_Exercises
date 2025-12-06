# Exercise 5: Check if the first and last numbers of a list are the same
# Write a code to return True if the list’s first and last numbers are the same.
# If the numbers are different, return False.

numbers = input()
numbers = list(numbers)
#print(type(numbers))
numbers_one = numbers[0]
numbers_last = numbers[-1]
if numbers_one == numbers_last:
    print(numbers_one, numbers_last, "True")
else:
    print("False")