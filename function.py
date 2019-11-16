# def get_int(msg):
#     while True:
#         try:
#             i = int(input(msg))
#             return i
#         except ValueError as err:
#             print(err)
#             continue
# age = get_int('enter your age: ')

import random
x = random.randint(1, 6)
y = random.choice((1, 5, 15, 30))
print(x)
print(y)