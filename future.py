import random
#гугл в помощь, захотел сделать рандомный баланс каждый раз
x = random.randrange(0, 1000000001, 10)

while True:
    try:
        y = int(input(f'U have {x} money, how many do u want to take? '))

        if y % 10 != 0:
            print('Only multiples of 10 allowed')
            continue

        if y > x:
            print('No.')
            continue

        x -= y
        print(f'You took {y}, left {x}')
        
    except ValueError:
        print('Dude like really wth is wrong with u?')

    repeat = input('Continue? Y/N: ')
    if repeat.lower() == 'n':
        break