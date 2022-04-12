class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._mass = 25
        self._unit = 5

    def calculate(self):
        print(int(self._length * self._width * self._mass * self._unit/1000), 'тон')


calc = Road(20, 5000)
calc.calculate()
