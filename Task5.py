"""5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
class Stationery:
    def __init__(self, title):
        print('Запуск отрисовки.')
    def draw(self):
        print('Рисует рисунок')

class Pen(Stationery):
    def draw(self):
        print('Рисует тонко, не стирается')


class Pencil(Stationery):
    def draw(self):
        print('Рисует тонко, стирается ')

class Handle(Stationery):
    def draw(self):
        print('Рисует толсто, не стирается')

s =  Stationery('Piska')
s.draw()
p= Pencil('pencil')
p.draw()