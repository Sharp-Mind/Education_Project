the_int = 15
the_str = 'Word'
the_bool = True
the_float = 1.25
the_list = [1, 2.25, True, 'String']
the_tuple = (1, 3.3, False, 'Hello')
the_dict = {'zip': '101000', 'address': 'Kremlin, 1'}

print(f"int: {the_int}\nstr: {the_str}\nbool: {the_bool}\nfloat: {the_float}\n"
      f"list: {the_list}\ntuple: {the_tuple}\ndict: {the_dict}")

user_str_input1 = input('\nВведите произвольный текст: ')
user_str_input2 = input('Введите ещё текст: ')
user_int_input = float(input('Введите целое число: '))
while not user_int_input.is_integer():
      user_int_input = float(input('Пожалуйста, повторите ввод. Нужно ввести целое чило: '))
user_int_input = int(user_int_input)
user_float_input = float(input('Введите дробное число: '))

print(f"\nВаш текст:\n\n{user_str_input1}\n{user_str_input2}\n\nВаши числа:\n\n{user_int_input}\n{user_float_input}")
