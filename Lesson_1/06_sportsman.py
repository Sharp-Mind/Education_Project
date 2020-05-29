a = float(input('Результат первого дня: '))
b = float(input('Цель: '))
i = 0

while a < b:
    a += 0.1 * a
    i += 1
i += 1

print(f'Цель будет достигнута на {i}-й день')