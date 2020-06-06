class Worker:

    name = ''
    surname = ''
    position = ''
    _income = {}

    def __init__(self, name, surname, position, wage=0, bonus=0):
        Worker.name = name
        Worker.surname = surname
        Worker.position = position
        Worker._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{Position.name} {Position.surname}'

    def get_total_income(self):
        return Position._income['wage'] + Position._income['bonus']



a = Position('Вася', 'Пупкин', 'Пекарь антиматерии', 50000, 5000)
print(a.get_full_name())
print(a.get_total_income())
