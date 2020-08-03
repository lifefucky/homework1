"""2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна.
Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""
class Road:
    _asphalt_weight=25
    _asphalt_height=5

    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)

    def calculate(self):
        result = self._length*self._width*self._asphalt_weight*self._asphalt_height/1000
        return result

r = Road(5000,20)
print(r.calculate())