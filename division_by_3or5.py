n = int(input('Enter the number: '))
lst = []

#solution_1
for i in range(n+1):
    if (i % 3 == 0) or (i % 5 == 0):
        lst.append(i)
        total = sum(lst)
print(total)

#solution_2
lst = [i for i in range(n+1) if (i % 3 == 0) or (i % 5 == 0)]
print(sum(lst))