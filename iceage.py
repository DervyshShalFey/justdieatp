while True:
    try:
        x = int(input('Dollars'))
        y = 0.87*x
        print(f'{x}Dollars = {y}Euroes')
    except ValueError:
        print('wth')
    finally:
        repeat = input('Continue? Y/N')
        if repeat.lower() == 'n':
                    break