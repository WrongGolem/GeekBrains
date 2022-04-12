import time


# Вариант импровизации:

class TrafficLight:

    def __init__(self, color_1, color_2, color_3):
        self.__color_1 = color_1
        self.__color_2 = color_2
        self.__color_3 = color_3

    def running(self):
        print(self.__color_1)
        time.sleep(7)
        print(self.__color_2)
        time.sleep(2)
        print(self.__color_3)
        time.sleep(5)


traffic = TrafficLight('Зеленый', 'Желтый', 'Красный')
traffic.running()


# Вариант согласно заданию:

class TrafficLight:

    def running(self):
        self.__color = 'Зеленый'
        print(f'{self.__color}')
        time.sleep(7)
        self.__color = 'Желтый'
        print(f'{self.__color}')
        time.sleep(2)
        self.__color = 'Красный'
        print(f'{self.__color}')
        time.sleep(5)


traffic = TrafficLight()
traffic.running()
