

def devision(dividend1, dividend2, divider):
    '''Делит параметры dividend1 и dividend2 поочерёдно на параметр divider.

    Именованные параметры:
    dividend1 -- первое делимое; тип float (обязательный аргумент)
    dividend2 -- второе делимоe; тип float  (обязательный аргумент)
    divider -- делитель; тип float  (обязательный аргумент)

    Возвращает:
    dividend1 / divider, dividend2 / divider
    '''
    return (dividend1 / divider), (dividend2 / divider)


def check_n_float(text=None):
    """Проверка вводимых данных. Проверяет локальную переменную data на соответствие типу данных float.

    Именованные параметры:
    text -- сообщение перед ожиданием ввода; тип любой (необязательный аргумент)


    Возвращает:
    float(data) -- Локальную переменную data, приведённую к типу данных float
    """
    while True:
        data = input(text)
        if data.lstrip('-').replace('.', '', 1).isdigit() == False:
            print('Пожалуйста, повторите ввод: нужно ввести натурально число')
        else:
            """
            Пункт проверки выше допупускает любое количество введённых знаков "минус", 
            поэтому здесь введена дополнительная проверка.
            """
            if data[0] == '-':  # for me: data[1] есть не всегда, сократить время выполнения таким способом не удастся
                data = data[0] + data.lstrip(data[0])
            print(data)
            return float(data)

user_input_1 = check_n_float('Введите первое делимое (дробная часть отделяется точкой): ')
user_input_2 = check_n_float('Введите второе делимое (дробная часть отделяется точкой): ')
user_input_3 = check_n_float('Введите делитель (дробная часть отделяется точкой): ')

# while True:
#     user_input_1 = input('Введите первый делимое: ')
#     if user_input_1.lstrip('-').replace('.', '', 1).isdigit() == False:
#         print('Пожалуйста, повторите ввод: нужно ввести натурально число')
#     else:
#         break
#
# while True:
#     user_input_2 = input('Введите второй делимое: ')
#     if user_input_2.lstrip('-').replace('.', '', 1).isdigit() == False:
#         print('Пожалуйста, повторите ввод: нужно ввести число')
#     else:
#         break
#
# while True:
#     user_input_3 = input('Введите второй делитель: ')
#     if user_input_3.lstrip('-').replace('.', '', 1).isdigit() == False:
#         print('Пожалуйста, повторите ввод: нужно ввести число')
#     else:
#         break

print(*(devision(user_input_1, user_input_2, user_input_3)))
