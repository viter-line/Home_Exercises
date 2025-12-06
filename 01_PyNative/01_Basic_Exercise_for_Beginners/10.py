list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

result_list = []

for i in list1:
    if i % 2 != 0:
        result_list.append(i)

for j in list2:
    if j % 2 == 0:
        result_list.append(j)

print(result_list)  