user_input = input('Введите число: ')

while not user_input.isdigit():
    user_input = input('Пожалуйста, повторите ввод. Нужно ввести число: ')

print(int(user_input) + int(user_input + user_input) + int(user_input + user_input + user_input))