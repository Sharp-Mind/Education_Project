class Stationery:
    title = ''

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    title = 'Ручка'

    def draw(self):
        print('Рисунок ручкой')


class Pencil(Stationery):
    title = 'Карандаш'

    def draw(self):
        print('Рисунок карандашом')


class Handle(Stationery):
    title = 'Маркер'

    def draw(self):
        print('Рисунок маркером')


for i in [Stationery(), Pen(), Pencil(), Handle()]:
    a = i
    a.draw()
