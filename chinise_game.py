number_of_sticks = int(input('Enter the number of sticks - '))
player = 1

def can_take(sticks):
    return sticks >= 1 and sticks <= 3

def switch_player_turn(turn):
    return 2 if player == 1 else 1

def end_of_game(sticks):
    return sticks <= 0

while (not end_of_game(number_of_sticks)):
    print(f'Take your sticks from {number_of_sticks} sticks')
    taken = int(input())

    if can_take(taken) == False:
        print('Forbidden! You can take 1,2 or 3 sticks')
        print()
        continue
    number_of_sticks -= taken
    print(f'Taken {taken} sticks\n')

    if end_of_game(number_of_sticks):
        print(f'Game is over. Player {player} won')
        break

    player = switch_player_turn(player)

# while number_of_sticks > 0:
#     print(f'Take your sticks from {number_of_sticks} sticks')
#     taken = int(input())
#     if taken < 1 or taken > 3:
#         print('Forbidden! You can take 1,2 or 3 sticks')
#         print()
#         continue
#     number_of_sticks -= taken
#     print(f'Taken {taken} sticks\n')

#     if number_of_sticks <= 0:
#         print(f'Game is over. Player {player} won')
#     else:
#         player = 1 if player == 2 else 2