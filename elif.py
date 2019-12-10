a = int(input('Enter the number: '))
b = int(input('Enter 1: B to Kb. Enter 2: Kb to B '))

if b == 1:
    print('{0} B it`s {1} Kb'.format(a, a//1000))
else:
    print('{0} Kb it`s {1} B'.format(a, a*1000))