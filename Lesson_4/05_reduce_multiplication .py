from functools import reduce

the_list = print(reduce(lambda x, y: x * y, [i for i in range(100, 1002, 2)]))
