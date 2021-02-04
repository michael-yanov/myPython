import random

ai_number = random.randint(1,50)
print(ai_number)
attempts = 1
print('Pay attention! You will have 6 attempts.')

while attempts < 7:
    print(f'Attempt number {attempts}')
    user_number = int(input('Enter your number: '))

    if user_number > ai_number:
        print('Your number is bigger. Try once again')
        print()
    elif user_number < ai_number:
        print('Your number is less. Try once again')
        print()
    else:
        print('Congrats! You won!')
        break
    attempts += 1