current_cards = [2, 3, 4, 10, 'Q', 5]
weight_cards = {
    2:    1,
    3:    1,
    4:    1,
    5:    1,
    6:    1,
    7:    0,
    8:    0,
    9:    0,
    10:  -1,
    'J': -1,
    'Q': -1,
    'K': -1,
    'A': -1
}
cards_sum = []

#solution_1
for x in current_cards:
    cards_sum.append(weight_cards[x])
print(sum(cards_sum))

#solution_2
cards_sum = sum([weight_cards[x] for x in current_cards])
print(cards_sum)
