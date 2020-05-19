
def statistics(name, surname, year, place, email, phone, act='in'):
    """Позволяет оперировать данными в списке из словарей, составленными из информации о людях.


    Именованные параметры:
    name -- подаваемое на ввод имя, тип str (обязательный параметр)
    surname -- подаваемая на ввод фамилия, тип str (обязательный параметр)
    year -- подаваемый на ввод год, тип str (обязательный параметр)
    place -- подаваемое на ввод место жительства (нахождения), тип str (обязательный параметр)
    email -- подаваемый на ввод адрес электронной почты, тип str (обязательный параметр)
    phone -- подаваемый на ввод номер телефона, тип str (обязательный параметр)
    act -- задаваемое пользователем действие, act='in' позволяет начать добавление данных, при act='out' - поиск
            по указанным данным (по умолчанию 'in'). Тип str, необязательный параметр.

    Переменные:
    inter_list -- кортеж из введённых пользователем данных, сделан для удобства поиска совпадений; тип tuple.
    default_keys -- словарь со стандартными ключами и пустыми значениями. Переменная out в словарях
                    служит маркером для вывода; тип dict.
    counter -- ориентировочный элемент механизма поиска совпадений, по нему определяется есть ли таковые между
               пользовательскими данными и имеющимися словарями; тип int.
    found -- элемент поиска совпадений при отборе словарей для вывода; тип bool

    Функция изменяет список словарей stat_dict или делает вывод из этого списка по найденным совпадениям в
    указанных данных.
    """

    inter_list = (surname, name, year, place, email, phone)  # для экономии памяти :)
    default_keys = {'фамилия': None, 'имя': None, 'год': None, 'город': None, 'e-mail': None, 'телефон': None,
                   'out': None}
    counter = 0
    found = False

    def add_info(action='new'):
        """Добавление или обновление словаря в списке.

        Именованные параметры:
        action -- обозначение добавления нового словаря; в этом случае добавляются ключи с пустым значением из
                  default_keys, тип string, необязательный параметр (по умолчанию = 'new')

        Добавляет в список словарей пользовательские данные
        """
        if action == 'new':
            stat_dict.append(default_keys)
        stat_dict[-1]['фамилия'] = inter_list[0]
        stat_dict[-1]['имя'] = inter_list[1]
        stat_dict[-1]['год'] = inter_list[2]
        stat_dict[-1]['город'] = inter_list[3]
        stat_dict[-1]['e-mail'] = inter_list[4]
        stat_dict[-1]['телефон'] = inter_list[5]


    if act == 'in':
        for one_dict in stat_dict:  # one_dict - это каждый словарь в листе
            for v in one_dict.values():
                for i in inter_list:
                    if v.count(i) > 0:
                        counter += 1

        if counter > 1:
            counter = 0
            while True:
                answer = input('Информация с такими данными уже существует. Заменить (R), добавить новую (N), '
                               'или отменить действие? (C)\n:> ')
                if answer.lower() == 'r' or answer.lower() == 'к':
                    for one_dict in stat_dict:
                        for v in one_dict.values():
                            for i in inter_list:
                                if v.count(i) > 0:
                                    counter += 1
                    if counter > 1:
                        add_info('replace')
                        print('Запись успешно заменена.')
                    break


                elif answer.lower() == 'n' or answer.lower() == 'т':
                    add_info()
                    print('Новая запись успешно добавлена.')
                    break
                elif answer.lower() == 'c' or answer.lower() == 'с':
                    print('Действие отменено пользователем.')
                    return
                else:
                    print('Ошибка ввода, попробуйте ещё раз.')

        else:
           add_info()

    elif act == 'out':
        for one_dict in stat_dict:
            for i in inter_list:
                for k in one_dict.keys():
                    if i in one_dict[k]:
                        one_dict['out'] = '1'

            print()
            for k in one_dict.keys():
                if one_dict['out'] == '1':
                    found = True
                    if k != 'out':
                        print((f' {k}: {one_dict[k]}.'), end='')

            one_dict['out'] = '0'

            if found == False:
                print('Совпадений не найдено.')
                break
        print('\n\nВывод закончен')

    return


stat_dict =[{'фамилия': 'Пупкин', 'имя': 'Вася', 'год': '2001', 'город': 'Энгельс', 'e-mail': '456@123.ru',
             'телефон': '89793331234', 'out': '0'},
            {'фамилия': 'Пупкин', 'имя': 'Вася', 'год': '2001', 'город': 'Энгельс', 'e-mail': '456@123.ru',
             'телефон': '89793331234', 'out': '0'},
            {'фамилия': 'Катя', 'имя': 'Мишина', 'год': '2002', 'город': 'Сочи', 'e-mail': '567@123.ru',
             'телефон': '83450009489', 'out': '0'}]

'''
Варианты ввода:
'''

statistics('Вася', 'Пупкин', '2987', 'Саратов', '123@123.ru', '89090001234')
# statistics('Женя', 'Пенькин', '2005', 'Владивосток', '456@123.ru', '89653332234')
# statistics('Вася', 'Пупкин', '1987', 'Саратов', '123@123.ru', '89090001234', 'out')
# statistics('Антон', 'Васин', '2003', 'Калуга', 'AntonV@gmail.com', '+79903344334', 'out')
