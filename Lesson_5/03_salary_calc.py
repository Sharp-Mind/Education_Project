# посложнее:

def check_float(data):
    while True:
        if data.lstrip('-').replace('.', '', 1).isdigit() == False:
            return False
        else:
            if data[0] == '-':
                data = data.lstrip('-')
            return True

total_salary = 0

with open('003.txt', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        if check_float(line.split()[1]):
            total_salary += float(line.split()[1])
            if round(float(line.split()[1]), 2) < 20000:
                print(line.split()[0])
        else:
            print(f'Ошибка формата в данных зарплаты сотрудника {line.split()[0]} \n')

'''
# попроще:

total_salary = 0
with open('003.txt', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        current_salary = float(line.split()[1])
        if float(current_salary) < 20000:
            print(line.split()[0])
        total_salary += current_salary

'''

print(f'\nСредняя з/п: {round(total_salary / len(lines), 2)}')
