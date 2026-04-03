list = []
try:
    while True:
        x = input('Add numbers, print s to stop')
        if x == 's': break
        x = int(x)
        list.append(x)
    print(f'Wow, they got {list[0]},', end = ' ')
    for i in range(len(list)-1):
        print(f'and {list[i+1]},', end = ' ')

except ValueError:
    print('uhhh')
except IndexError:
    print('Empty, lol')   
finally:
    print('gg')         