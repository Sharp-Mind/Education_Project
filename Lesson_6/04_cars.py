from random import uniform, choice


class Car:

    speed = 140
    color = 'Gray'
    name = 'Car1'
    is_police = False

    def show_speed(self):
        self.speed = f'{uniform(0, Car.speed):.2f}'
        print(self.speed)

    def go(self):
        self.go_conditon = ('Started', 'Idle')
        print(choice(self.go_conditon))

    def stop(self):
        self.stop_conditon = ('Stops', 'Is moving')
        print(choice(self.stop_conditon))

    def turn_direction(self):
        self.turn_conditon = ('Turns left', 'Goes straight', 'Turns right')
        print(choice(self.turn_conditon))


class TownCar(Car):

    color = 'White'
    name = 'Fleetwood'
    speed_limit = 60

    def show_speed(self):
        super().show_speed()
        if float(self.speed) > TownCar.speed_limit:
            print("Warning! You're speeding!")


class SportCar(Car):

    speed = 250
    color = 'Silver'
    name = 'R33'

class WorkCar(Car):

    Speed = 95
    color = 'Green'
    name = 'Kaa'
    speed_limit = 40

    def show_speed(self):
        super().show_speed()
        if float(self.speed) > WorkCar.speed_limit:
            print("Warning! You're speeding!")


class PoliceCar(Car):

    speed = 220
    color = 'Police'
    name = 'Crown Victoria Police Interceptor'
    is_police = True


a = TownCar()
a.show_speed()
a = WorkCar()
a.show_speed()
a.go()
a.turn_direction()
a.stop()
