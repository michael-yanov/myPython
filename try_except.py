a = input('type first here - ')
b = input('type second here - ')
try:
    a_num = float(a)
    b_num = float(b)
    c = a_num + b_num
    print('the number is - ', c)
except:
    # a = str(a)
    # b = str(b)
    # c = a + b
    print('the string is - ', a + b)