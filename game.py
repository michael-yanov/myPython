import random

while True:
    gamer_turn = str(input('Make your choice: R/S/P - ').upper())
    print(f'Your choice is {gamer_turn}')

    ai_turn = random.choice(['R', 'S', 'P'])
    print(f'AI choice is {ai_turn}')

    if gamer_turn == ai_turn:
        print('It\'s draw')
    elif (gamer_turn == 'R' and ai_turn == 'S') or (gamer_turn == 'S' and ai_turn == 'P') or (gamer_turn == 'P' and ai_turn == 'R'):
        print('Congrats! You won')
    else:
        print('AI won')
    
    game = input('Do you want to continue? [Y/n]: ')
    print()
    if game == '' or game == 'y':
        continue
    else:
        break
