# Используемый файл:
'''
Информатика: 100(л) 50(пр) 20(лаб)
Изо: 10(л) 30(пр) -
Физика: 30(л) - 10(лаб)
Физкультура: - 30(пр)
Русский язык: 50(л) 70(пр) -
Черчение: 20(л) 40(пр) -
Химия: 65(л) - 40(лаб)
Литература: 55(л) 15(пр) -
'''

with open('006.txt', encoding='utf-8') as file:
    lines = file.readlines()

out_dict = {}

for line in lines:
    total = 0
    for word in line.split():
        mid_string = ''
        for symbol in word:
            if symbol.isdigit():
                mid_string += symbol
        if mid_string.isdigit():
            total += int(mid_string)
    if len(line.split()) == 5:
        out_dict[f'{line.split()[0]} {line.split()[1]}'] = total
    else:
        out_dict[line.split()[0]] = total

print(out_dict)
