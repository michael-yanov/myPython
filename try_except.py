a = input('enter the first digit here - ')
b = input('enter the second digit here - ')
try:
    if (a != '') and (b != ''):
        a = float(a)
        b = float(b)
        c = input('type action here - ')
        if c == '+':
            print(a + b)
        elif c == '-':
            print(a - b)
        elif c == '*':
            print(a * b)
        elif c == '/':
            print(a / b)
except TypeError:
    print('you need to enter two digits')
except ZeroDivisionError:
    print('you can`t type zero')
