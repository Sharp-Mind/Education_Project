from itertools import cycle

rainbow = ('каждый', 'охотник', 'желает', 'знать', 'где', 'сидит', 'фазан')

for i in cycle(range(len(rainbow))):
    print(rainbow[i])
    if i == len(rainbow) - 1:
        break
