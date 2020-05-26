with open('001.txt', 'w') as file:
    user_input = None
    while user_input != '':
        user_input = input('Введите строку: ')
        file.write(user_input + '\n')

print('Конец')
