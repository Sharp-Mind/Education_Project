from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, dimension):
        if str(dimension).replace('.', '', 1).isdigit() == True:
            self._dimension = float(dimension)
        else:
            raise ArithmeticError('Wrong square value!')

    def cloth(self):
        return f'{(self._dimension / 6.5) + 0.5:.2f}'

    @abstractmethod
    # @property
    def square(self):
        return self._dimension

    @abstractmethod
    # @square.setter
    def square(self, value):
        self._dimension = value


class Coat(Clothes):

    @property
    def square(self):
        return self._dimension

    @square.setter
    def square(self, value):
        self._dimension = value

    def cloth(self):
        return f'{(self._dimension / 6.5) + 0.5:.2f}'


class Suit(Clothes):

    @property
    def square(self):
        return self._dimension

    @square.setter
    def square(self, value):
        self._dimension = value

    def cloth(self):
        return f'{(self._dimension * 2) + 0.3:.2f}'


a = Coat(5)
a.square = 10
print(a.square)
print(a.cloth())
b = Suit(10)
print(b.cloth())
