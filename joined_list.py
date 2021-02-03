list_1 = [1,2,3,4,5,6]
list_2 = [11,12,13,14,15,16]
joined_list = []

#solution_1
for x in list_1:
    if x % 2 != 0:
        joined_list.append(x)
for y in list_2:
    if y % 2 == 0:
        joined_list.append(y)
print(joined_list)

#solution_2
odd = [x for x in list_1 if x % 2 != 0]
even = [y for y in list_2 if y % 2 == 0]
joined_list = odd + even
print(joined_list)