a = input('enter the first digit here - ')
b = input('enter the second digit here - ')
if (a != '') and (b != ''):
    try:
            a = float(a)
            b = float(b)
            c = input('enter action here - ')
            if c == '+': print(a + b)
            elif c == '-': print(a - b)
            elif c == '*': print(a * b)
            elif c == '/': print(a / b)
    except ZeroDivisionError:
        print('ERROR')
else:
    print('ERROR, please enter two digits')
