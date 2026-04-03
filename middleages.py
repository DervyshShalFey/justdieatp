x = input('Numbers:')
z = 0
try:
    y = x.split()
    for i in range(len(y)):
        y[i] = int(y[i])
        z += y[i]
        
    print(f'{z}-sum')
    print(f'{z/len(y)}-middle')
except ValueError:
    print('not a number')
except IndexError:
    print('empty lol')
else:
    print('done, ig')
