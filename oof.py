operators = ['+','-','*','/']


while(True):
    try: 
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number:'))
        action = input('Enter operation (+, -, *, /):')
        if action not in operators:
             raise Exception(action)

        match action:
            case '+': print(f'{num1} + {num2} = {num1 + num2}')
            case '-': print(f'{num1} - {num2} = {num1 - num2}')
            case '*': print(f'{num1} * {num2} = {num1 * num2}')
            case '/': print(f'{num1} / {num2} = {num1 / num2}')
    except ZeroDivisionError:
        print('Не можна ділити на 0!')
    except ValueError:
        print('cant touch this!')
    except Exception as ex:
        print(f'no {ex.args[0]}')
    finally:
        repeat = input('Continue? Y/N')
        if repeat.lower() == 'n':
                    break