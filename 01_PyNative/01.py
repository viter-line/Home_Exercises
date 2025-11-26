# Given two integer numbers,
# write a Python program to return their product
# only if the product is equal to or lower than 1000.
# Otherwise, return their sum.
a = int(input("First number: "))
b = int(input("Second number: "))

if a * b <= 1000:
    print(a*b)
elif a * b > 1000:
    print(a+b)

# number1 = int(input("Enter number 1: "))
# number2 = int(input("Enter number 2: "))
# print("number1 =", number1)
# print("number2 =", number2)
#
# if number1 * number2 >= 1000:
#     print("The result is",number1 + number2)
# else:
#     print(number1 * number2)