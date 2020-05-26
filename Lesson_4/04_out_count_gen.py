source = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

[print(i, end=' ') for i in source if source.count(i) == 1]

'''
# или с записью списка в переменную:

the_list = [i for i in source if source.count(i) == 1]

# или перезапись:

source = [i for i in source if source.count(i) == 1]
'''