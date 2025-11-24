a = input()

print(type(a))

a = list(a)
print("Only even index chars:")
for i in a[0::2]:
    print(i)