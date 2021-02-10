def whois_first(p1, p2):
    #case_1 using lstrip finction
    p1_count_spaces = (len(p1) - len(p1.lstrip(' ')))
    p2_count_spaces = (len(p2) - len(p2.lstrip(' ')))
    if p1_count_spaces > p2_count_spaces:
        return print('p2')
    elif p1_count_spaces < p2_count_spaces:
        return print('p1')
    else:
        return print('tie')

    #case_1 using index function
    if p1.index('B') > p2.index('B'):
        return print('p2')
    elif p1.index('B') < p2.index('B'):
        return print('p1')
    else:
        print('tie')

whois_first('    BANG!  ','     BANG!   ')

