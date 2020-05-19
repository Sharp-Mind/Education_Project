numbers = 0
user_quit = False

def check_float(data):
    """Проверка вводимых данных. Проверяет локальную переменную data на соответствие типу данных float.

        Именованные параметры:
        data -- входные данные от пользователя; тип str (обязательный аргумент)

        Возвращает:
        True, если проверка пройдена и определён тип данных float, иначе возвращает False.
    """
    while True:
        if data.lstrip('-').replace('.', '', 1).isdigit() == False:
            return False
        else:
            if data[0] == '-':
                data = data[0] + data.lstrip(data[0])
            return True


def sum_string(the_string):
    """Суммирует числа в строке, до ввода символа 'q'.

    Именованные параметры:
    the_string -- строка пользователького ввода; тип str (обязательный параметр).

    Возвращает:
    Сумму чисел в строке через локальную переменную out, если проверка на float пройдена, иначе возвращает 0 (тип int).
    """
    out = 0
    the_string = the_string.replace(' ', '0')
    for i in the_string:
        if not (check_float(i) or i.lower() == 'q'):
            print('Вы ввели не числа! Ничего не было прибавлено.')
            return 0
        else:
            for i in range(len(tuple(the_string))):
                if the_string[i].lower() == 'q':
                    global user_quit
                    user_quit = True
                    break
                else:
                    out += float(the_string[i])
            return out


while user_quit == False:
    user_input = input('Введите числа в строку через пробел или "q" чтобы закончить: ')
    numbers += sum_string(user_input)
    print('Итоговая сумма равна ', numbers, '\n')
print('Совершён выход по запросу пользователя.')
