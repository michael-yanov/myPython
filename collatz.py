def collatz(number):
    if number % 2 == 0:
        return  number // 2
    else:
        return 3 * number + 1

while True:
    try:
        num = int(input('Enter a number: '))
        t = collatz(num)
        print(t)
        if t == 1:
            break
    except ValueError as err:
        print('Wrong format. You need to enter integer.', err)
    
