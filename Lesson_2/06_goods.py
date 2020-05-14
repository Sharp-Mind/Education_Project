goods = [(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
        (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
        (3, {'название': 'принтер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})]

analytics = {}

for i in range(len(goods)):
    for k in goods[i][1].keys():
        if k not in analytics:
            analytics[k] = []
        if i > 0 and goods[i][1][k] in analytics[k]:  # если требуется уникальность элементов с списке значения
            continue
        else:
            analytics[k].append(goods[i][1][k])


for k in analytics.keys():
    print(f'{k}: {analytics[k]}')
