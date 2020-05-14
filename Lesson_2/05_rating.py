the_list = [9, 7, 5, 3, 3, 2]

while True:
    user_data = input('Введите одно натуральное число: ')
    if not user_data.isdigit() or int(user_data) < 1:
        print('Нужно ввести одно целое число больше нуля.')
    else:
        user_data = int(user_data)
        if user_data > the_list[0]:
            the_list.insert(0, user_data)
        elif user_data < the_list[-1]:
            the_list.append(user_data)
        else:
            for i in range(len(the_list)):
                if the_list[i] == user_data:
                    the_list.insert(i, user_data)
                    break
                elif (the_list[i] > user_data > the_list[i + 1]):
                    the_list.insert(i + 1, user_data)
                    break
        print(the_list)
        break
