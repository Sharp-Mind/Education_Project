class Cell:
    def __init__(self, quantity):
        if isinstance(quantity, int):
            self._quantity = quantity
            if self._quantity <= 0:
                raise ValueError('Cell type must to assign int values greater than zero!')
        else:
            raise ValueError('Cell type must to assign int values!')

    def __add__(self, other):
        return Cell(self._quantity + other._quantity)

    def __sub__(self, other):
        if self._quantity > other._quantity:
            return Cell(self._quantity - other._quantity)
        else:
            raise ArithmeticError('It is necessary to subtract the smaller cell from the larger cell!')

    def __mul__(self, other):
        return Cell(self._quantity * other._quantity)

    def __truediv__(self, other):
        return Cell(self._quantity // other._quantity)

    def __str__(self):
        return str(self._quantity)

    def make_order(self, quan_per_row):
        if isinstance(quan_per_row, int):
            self._quan_per_row = quan_per_row
            self.__roundquan = self._quantity // self._quan_per_row
            return ('*' * self._quan_per_row + '\n') * self.__roundquan + '*' * (self._quan_per_row - self.__roundquan)
        else:
            raise ValueError('The "make_order" function supports only int values!')



a, b = Cell(15), Cell(12)
print((a + b).make_order(6) + '\n')
c = a * b
print(c.make_order(22) + '\n')
print(a / b)
print(a - b)
