from random import randint

with open('005.txt', 'w+') as file:
    [file.write(str(randint(0, 30)) + ' ') for i in range(10)]
    file.seek(0)
    line = file.readline()

total = 0
for i in line.split():
    total += int(i)

print(f'Сумма чисел в файле: {total}')
