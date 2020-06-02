from random import randint


class Matrix:
    def __init__(self, input_list):
        for i in range(len(input_list)):
            if len(input_list[i]) != len(input_list[0]):
                raise ArithmeticError('Wrong matrix size!')
            else:
                self._matrix = input_list

    def __str__(self):
        self._output = ''

        '''Подсчёт выравнивания матрицы для вывода моноширинным шрифтом'''

        self.max_el_len = 0
        for i in self._matrix:
            for j in i:
                if len(str(j)) > self.max_el_len:
                    self.max_el_len = len(str(j))

        '''Конец подсчёта'''

        for i in self._matrix:
            self._output += '\n'
            for j in i:
                if len(str(j)) < self.max_el_len:
                    self._output += (self.max_el_len - len(str(j))) * ' ' + str(j) + ' '
                else:
                    self._output += f'{j} '
        return self._output



    def __add__(self, other):
        self._matrix_summ = [[0 for j in range(len(self._matrix[i]))] for i in range(len(self._matrix))]
        for string in range(len(self._matrix)):
            if len(self._matrix) != len(other._matrix) or len(self._matrix[string]) != len(other._matrix[string]):
                raise ArithmeticError('Unable to perform operation with different matrix sizes!')
            for num in range(len(self._matrix[string])):
                self._matrix_summ[string][num] += self._matrix[string][num] + other._matrix[string][num]

        return Matrix(self._matrix_summ)


a = Matrix([[randint(0, 50) for i in range(3)] for j in range(3)])
b = Matrix([[randint(0, 50) for i in range(3)] for j in range(3)])
c = Matrix([[randint(0, 50) for i in range(3)] for j in range(3)])
print(a + b + c)

''' Пример вывода ошибки с матрицами разной размерности: '''
# d = Matrix([[randint(0, 99) for i in range(2)] for j in range(3)])
# e = Matrix([[randint(0, 99) for i in range(3)] for j in range(3)])
# print(d + e)