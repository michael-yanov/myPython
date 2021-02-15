def recursia(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return 2**x - 1

print(recursia(7))

