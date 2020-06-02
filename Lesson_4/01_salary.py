from sys import argv

if len(argv) < 4:
    print('Недостаточно данных для вычисления!')
else:
    if len(argv) > 4:
        print('Только первые три введённых значения участвуют в рассчётах; остальные будут проигнорированы.')
    try:
        productivity = argv[1]
        rate = argv[2]
        bonus = argv[3]
        print(round((float(productivity) * float(rate)) + float(bonus), 2))
    except ValueError:
        print('Переданы не числа или не только числа!')
