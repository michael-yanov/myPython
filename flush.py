table_cards = ['A_S', 'J_D', '7_S', '8_D', '10_D']
hand_cards = ['J_D', '3_D']
joined_list = []

for x in table_cards:
    joined_list.append(x[-1])
for y in hand_cards:
    joined_list.append(y[-1])
flush = False

for i in 'CHSD':
    if joined_list.count(i) >= 5:
        flush = True

if flush:
    print('Flush')
else:
    print('No Flush')