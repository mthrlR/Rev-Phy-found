# Easy


# Task one
"""
class towncar:

    def __init__(self, speed, colour, name, is_police=False):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} поехала!'.format(self.name))

    def stop(self):
        print('{} остановались!'.format(self.name))

    def turn(self, direction):
        print('{} повернула {}!'.format(self.name, direction))


class sportcar:
    def __init__(self, speed, colour, name, is_police=False):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} поехала!'.format(self.name))

    def stop(self):
        print('{} остановались!'.format(self.name))

    def turn(self, direction):
        print('{} повернула {}!'.format(self.name, direction))


class workcar:
    def __init__(self, speed, colour, name, is_police=False):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} поехала!'.format(self.name))

    def stop(self):
        print('{} остановались!'.format(self.name))

    def turn(self, direction):
        print('{} повернула {}!'.format(self.name, direction))


class policecar:
    def __init__(self, speed, colour, name):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = True

    def go(self):
        print('{} поехала!'.format(self.name))

    def stop(self):
        print('{} остановались!'.format(self.name))

    def turn(self, direction):
        print('{} повернула {}!'.format(self.name, direction))

sportcar = sportcar(120, 'красная', 'спортивная машина')
towncar = towncar(60, 'черная', 'обычная машина')
workcar = workcar(7, 'желтая', 'спец техника')
policecar = policecar(125, 'бело-синяя', 'полиция')

print(workcar.name)
"""
# Task two
"""
class car:
    def __init__(self, speed, colour, name):
        self.speed = speed
        self.color = colour
        self.name = name
        self.is_police = False

    def go(self):
        print('{} поехала!'.format(self.name))

    def stop(self):
        print('{} остановались!'.format(self.name))

    def turn(self, direction):
        print('{} повернула {}!'.format(self.name, direction))


class towncar(car):
    pass


class sportcar(car):
    pass


class workcar(car):
    def __init__(self, speed, colour, name, yellow_siren=True):
        super().__init__(speed, colour, name)
        self.yellow_siren = yellow_siren


class policecar(car):
    def __init__(self, speed, colour, name):
        super().__init__(speed, colour, name)
        self.is_police = True

sportcar = sportcar(120, 'красная', 'спортивная машина')
towncar = towncar(60, 'черная', 'обычная машина')
workcar = workcar(7, 'желтая', 'спец техника')
policecar = policecar(125, 'бело-синяя', 'полиция')

print(workcar.yellow_siren)
"""