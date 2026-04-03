x = input('Enter the number of ur ticket:')
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
try:
    if x[0:3] == 'ORD' and x[3:] in list:
        pass
    else:
        raise Exception


except Exception:
    print('no such a ticket bro')

else:
    print('checked!')
