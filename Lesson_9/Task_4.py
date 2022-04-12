class Car:
    is_police = False

    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.speed = 0

    def go(self, speed=35):
        self.speed = speed
        print(f'Автомобиль {self.name} начал движение со скоростью {self.speed} км/ч')

    def stop(self):
        self.speed = 0
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):
        if direction == 'влево' or direction == 'вправо':
            print(f'Автомобиль {self.name} повернул {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} составляет {self.speed} км/ч')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость автомобиля {self.name} составляет {self.speed} км/ч,что выше разрешенной')
        else:
            print(f'Скорость автомобиля {self.name} составляет {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость автомобиля {self.name} составляет {self.speed} км/ч,что выше разрешенной')
        else:
            print(f'Скорость автомобиля {self.name} составляет {self.speed} км/ч')


class PoliceCar(Car):
    is_police = True


auto_1 = PoliceCar('Черный', 'Ford')
auto_1.go(20)
auto_2 = SportCar('Красный', 'Ferrari')
auto_2.go(80)
auto_2.show_speed()
auto_2.turn('влево')
auto_3 = WorkCar('Белый', 'Mercedec')
auto_3.go(70)
auto_3.show_speed()
auto_4 = TownCar('Серебристый', 'Daewoo')
auto_4.go(60)
auto_4.show_speed()
auto_4.stop()
auto_4.show_speed()
