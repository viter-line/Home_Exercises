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
