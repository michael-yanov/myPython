# n = input('Enter an integer: ')
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print('Wrong input!')
#         n = input('Enter an integer: ')
# if n % 2 == 0:
#     print('Even')
# else:
#     print('Odd')
#---------------------------------------------------------

# total = 100
# i = 0
# while i < 5:
#     n = int(input())
#     total = total - n
#     i = i + 1
# print('Ostalos ', total)
#---------------------------------------------------------

# total = 100
# while total > 0:
#     n = int(input('Enter an integer: '))
#     if n <= total:
#         total = total - n
#     else:
#         print('Operation is not allowed')
#         break
# print(total)

i = -3
while i < 20:
    i = i + 1
    n = 2 ** i
    print('2 in', i, '=', n)