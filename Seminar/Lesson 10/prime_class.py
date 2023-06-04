class Car:
    # class_atr = 0


    def __init__(self, label: str, color: str, year: int, audio: str = 'Нет'):
        self.label = label
        self.color = color
        self.year = year
        self.audio = audio


    def __str__(self):
        return f'Машина марки: {self.label}, цвет: {self.color}, {self.year} года выпуска'


    def drive(self):
        print('skr-skr-skr')


car = Car('Mazda', 'Красный', 2015)

new_car = Car('Mercedes', 'Черный', 2023)

old_car = Car('ВАЗ 2101', 'Зеленый', 1967)

old_car.audio = "DOLBIT NORMAL'NO))0)"

print(car)
print(new_car)
print(old_car)
