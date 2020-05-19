income = float(input('Введите сумму дохода: '))
costs = float(input('Введите сумму издержек: '))
profit = income - costs

if profit > 0:
    print('\nВаша фирма работает в прибыль!')
    print(f'Рентабельность выручки: {round((profit / income * 100), 2)}\n')
    print('Прибыль на одного сотрудника:', round(profit / int(input('Введите количество сотрудников: ')), 2))
elif profit == 0:
    print('\nДоходы вашей фирмы равны расходам!')
elif profit < 0:
    print('\nВаша фирма работает в убыток!')

# здесь решил сделать без проверок ввода