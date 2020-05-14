user_input = input('Введите целое положительное число: ')

while not (user_input.isdigit() and int(user_input) > 0):
    user_input = input('Пожалуйста, убедитесь, что вводите правильно. Введите целое положительное число: ')

i = 0
max_num = int(user_input[i])

while i != len(user_input):
    if int(user_input[i]) > max_num:
        max_num = int(user_input[i])
    i += 1

'''
# Оно же через цикл "For":

max_num = int(user_input[0])
for i in user_input:
    if int(i) > max_num:
        max_num = int(i)
'''

print('Наибольшая цифра в введённом числе: ', max_num)
