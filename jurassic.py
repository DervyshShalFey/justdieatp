try:
    num1 = int(input('value'))
    num2 = int(input('sale'))
    num3 = num1*(1-num2/100)
    if num2> 100 or num2<100:
        print('uhhhhh')
        
    else:
        print(num3)
except ValueError:
    print('woah, chill bro')

