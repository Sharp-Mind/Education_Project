list_1 = input('Введите слова или цифры, разделяя их через пробел: ').split()

for i in range(0, (len(list_1) - 1 if len(list_1) % 2 != 0 else len(list_1)), 2):
    list_1[i], list_1[i + 1] = list_1[i + 1], list_1[i]

print(list_1)
