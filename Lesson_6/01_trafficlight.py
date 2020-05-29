from time import sleep
from itertools import cycle

class TrafficLight:

    __color = ['красный', 'жёлтый', 'зелёный']

    def running(self):
        for i in cycle(range(len(TrafficLight.__color))):
            print(TrafficLight.__color[i])
            if i == 0 or i == 2:
                sleep(7)
            else:
                sleep(2)


a = TrafficLight()
a.running()
