def calc_dice_scores(lst):
    new_lst = []
    for i, j in lst:
        if i == j:
            return print('0')
        else:
            new_lst.append(i+j)
    return print(sum(new_lst))

score = calc_dice_scores([(4 ,5), (4, 4), (5, 6)])
