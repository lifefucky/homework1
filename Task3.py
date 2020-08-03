"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name,
surname,
position (должность),
income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад
премия,
например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения
полного имени сотрудника (get_full_name)
дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:
    def __init__(self, name,surname, position,wage, bonus):
        self.name=name
        self.surname=surname
        self.position=position
        self._income = {'wage': wage, 'bonus':bonus}

    def get_full_name(self):
        return f'{self.name} {self.surname}'
    def get_total_income(self):
        result_income = sum(self._income.values())
        return result_income

class Position(Worker):
    def __init__(self, name:str, surname:str, position:str, wage:float, bonus:float):
        #self.position_name = position_name
        super().__init__(name, surname, position, wage, bonus)



tmp = Position('Александр', 'Родионович', 'Охранник', 5000, 228)
print(tmp.get_full_name())
print(tmp.get_total_income())
