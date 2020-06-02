seasons_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
                'ноябрь', 'декабрь']
seasons_dict = {1: seasons_list[0], 2: seasons_list[1], 3: seasons_list[2], 4: seasons_list[3], 5: seasons_list[4],
                6: seasons_list[5], 7: seasons_list[6], 8: seasons_list[7], 9: seasons_list[8], 10: seasons_list[9],
                11: seasons_list[10], 12: seasons_list[11]}

while True:
    user_input = input('Введите номер месяца: ')
    if not user_input.isdigit() or int(user_input) not in range(1, 13):
        print('Нужно ввести только число от 1 до 12. Повторите ввод.')
    else:
        # Через список:
        # print(f"Это {seasons_list[int(user_input) - 1]}")

        # Через словарь:
        print(f"Это {seasons_dict[int(user_input)]}.")
        break
