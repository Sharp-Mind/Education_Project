from random import random, shuffle

rolled = []
number_of_kegs = 90


class Gamer:
    def __init__(self):

        self.nums_per_line = 5
        self.player_card = [['----------Gamer-----------'], ['   ', '   ', '   ', '   '], ['   ', '   ', '   ', '   '],
                       ['   ', '   ', '   ', '   '], ['--------------------------']]

    def roll(self):
        yield round(random() * (90 - 1) + 1)

    def give_me_num(self):
        for self.__el in self.roll():
            return self.__el

    def fill_card(self):
        self.__card_num = self.give_me_num()
        self._total_in_card = []
        for line in range(len(self.player_card) - 2):
            self.__needed = []
            for i in range(self.nums_per_line):
                while self.__card_num in self._total_in_card:
                    for el in self.roll():
                        self.__card_num = el
                if self.__card_num < 10:
                    self.__card_num = ' ' + str(self.__card_num)
                self.__needed.append(str(self.__card_num) + ' ')
                self._total_in_card.append(self.__card_num)

            self.player_card[line + 1].extend(self.__needed)
            shuffle(self.player_card[line + 1])


    def step(self, current_num):
        self._found = False
        self.__current_num = current_num
        self.user_answer = input('Зачеркнуть? (у/n): ').lower()
        if self.__current_num == 0:
            print('Бочонков больше не осталось!')
            return False
        for i in range(1, len(self.player_card)):
            for j in self.player_card[i]:
                if str(self.__current_num).rstrip() in j:
                    if self.__current_num < 10 and len(j.rstrip().lstrip()) == 1 or\
                            (self.__current_num >= 10 and len(j.rstrip().lstrip()) == 2):
                        self._found = True
                        if self.user_answer == 'y':
                            self.player_card[i][self.player_card[i].index(j)] = '-- '
                            if self.__current_num < 10:
                                del self._total_in_card[
                                        self._total_in_card.index(' ' + str(self.__current_num))]
                                break
                            elif  self.__current_num >= 10:
                                del self._total_in_card[
                                    self._total_in_card.index(self.__current_num)]
                                break

        if (self.user_answer == 'n' and self._found == True) or (self.user_answer == 'y' and self._found == False):
            print('Вы проиграли!')
            return False

    def check_win(self):
        if len(self._total_in_card) == 0:
            return True


class Player(Gamer):
    def __init__(self):
        super().__init__()
        self.player_card[0] = ['----------Player----------']

    def num_from_bag(self):
        self._num = self.give_me_num()
        if len(rolled) >= 90:
            return 0

        while self._num in rolled:
            self._num = self.give_me_num()
        rolled.append(self._num)
        return self._num


class Computer(Gamer):
    def __init__(self):
        super().__init__()
        self.player_card[0] = ['---------Computer---------']

    def step(self, current_num):
        self.__current_num = current_num
        for i in range(1, len(self.player_card)):
            for j in self.player_card[i]:
                if str(self.__current_num) in j:
                    if self.__current_num < 10 and len(j.rstrip()) == 1:
                        self.player_card[i][self.player_card[i].index(j)] = '-- '
                        del self._total_in_card[
                            self._total_in_card.index(' '+ str(self.__current_num))]
                    elif self.__current_num >= 10 and len(j.rstrip().lstrip()) == 2:
                        self.player_card[i][self.player_card[i].index(j)] = '-- '
                        del self._total_in_card[
                            self._total_in_card.index(self.__current_num)]
                    break


a = Player()
b = Computer()
a.fill_card()
b.fill_card()

while len(rolled) <= number_of_kegs:

    print()
    [[print(j, end='') for j in i] and print() for i in a.player_card]
    print('==========================')
    [[print(j, end='') for j in i] and print() for i in b.player_card]

    keg = a.num_from_bag()
    print(f'Выпал бочонок с номером {keg}')

    if a.step(keg) == False:
        break
    elif a.check_win() == True:
        print('Игрок победил!')
        break
    elif b.check_win() == True:
        print('Компьютер победил!')
        break
    b.step(keg)
