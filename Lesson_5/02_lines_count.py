with open('002.txt') as file:
    lines = file.readlines()
    lines_count,  words_count = 0, 0
    for line in lines:
        for word in line.split():
            words_count += 1
        lines_count += 1

# print(f'Количество строк: {lines_count}, количество слов: {words_count}')
