s_circle = 0


def cylinder():
    def circle():
        global s_circle
        s_circle = 3,14 * r ** 2
        r = int(input('Enter the radius: '))
        h = int(input('Enter the high: '))
        if (print(input('1 - halh, 2 - full'))) == 1:
            s_cylindre = 2 * 3,14 * r * h
        else:
            circle()
            s_cylindre = 2 * s_circle
        print(s_cylindre)


cylinder()