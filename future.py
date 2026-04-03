import random
#гугл в помощь, захотел сделать рандомный баланс каждый раз
x = random.randrange(0, 1000000001, 10)

while True:
    try:
        y = int(input(f'U have {x} money, how many do u want to take out?'))

        if y%10 != 0:
            print('Only 10s kiddo')
            pass

        if y>x:
            print('No.')
            pass

        x -= y
        print(f'You took {y}, left {x}')
        
    except ValueError:
        print('Dude like really wth is wrong with u?')

    repeat = input('Continue? Y/N: ')
    if repeat.lower() == 'n':
        break