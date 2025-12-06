income = int(input("Enter your income: "))

if income <= 10000:
    tax_rate = 0
elif income <= 20000:
    x = income - 10000
    tax_rate = x * 10/100
else:
    tax_rate = 0
    tax_rate = 10000 * 10/100
    tax_rate += (income - 20000) * 20/100

print("Your tax is:", tax_rate) 