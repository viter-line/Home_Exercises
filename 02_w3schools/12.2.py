# 12. Python Tuples
# Convert a tuple to a list, add an element, and convert it back to a tuple.

t = (1, 2, 3)
lst = list(t)
lst.append(4)
t = tuple(lst)
print(t)