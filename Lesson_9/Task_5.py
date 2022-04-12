class Stationery:
    def __init__(self, title='Draw something'):
        self.title = title

    def draw(self):
        print(f'Just do it! {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Draw  with a {self.title} pen!')


class Pencil(Stationery):
    def draw(self):
        print(f'Draw with a {self.title} pencil!')


class Marker(Stationery):
    def draw(self):
        print(f'Draw with a {self.title} marker!')


stat = Stationery()
stat.draw()
pen = Pen('Parker')
pen.draw()
pencil = Pencil('Luos&Stark')
pencil.draw()
marker = Marker('Fantik')
marker.draw()
