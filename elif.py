x = input('Enter number here: ')
try:
    x = float(x)
    if x > 0:
        print('1')
    elif x == 0:
        print('0')
    else:
        print('-1')
except ValueError:
    print('ERROR - Enter a number')
# old = input('Your age: ')
# try:
#     old = int(old)
#     print('Рекомендовано:', end=' ')
#     if 3 <= old < 6:
#         print('"Заяц в лабиринте"')
#     elif 6 <= old < 12:
#         print('"Марсианин"')
#     elif 12 <= old < 16:
#         print('"Загадочный остров"')
#     elif 16 <= old:
#         print('"Поток сознания"')
#     else:
#         print('You are too small for watching TV')
# except ValueError:
#     print ('ERROR - You need to enter integer')