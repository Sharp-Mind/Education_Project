class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        Road._length = float(length)
        Road._width = float(width)

    def mass_calc(self):
        return Road._length * Road._width * 25 * 0.05


a = Road(20, 4545.3)
print(a.mass_calc())
