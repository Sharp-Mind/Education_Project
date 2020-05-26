user_time = int(input('Пожалуйста, введите количество секунд: '))
zero_1, zero_2, zero_3 = '', '', ''

seconds = user_time % 60
hours = user_time // 3600
minutes = (user_time // 60) - (60 * hours)

if hours < 10:
    zero_1 = 0

if seconds < 10:
    zero_2 = 0

if minutes < 10:
    zero_3 = 0
'''
# Вариант 2:
if hours < 10:
    hours = '0' + str(hours)

if seconds < 10:
    seconds = '0' + str(seconds)

if minutes < 10:
    minutes = '0' + str(minutes)
'''

print(f"Это же время в часах, минутах и секундах: {zero_1}{hours}:{zero_2}{minutes}:{zero_3}{seconds}")

