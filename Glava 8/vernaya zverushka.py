# Программа "Классово верная зверюшка"
# Демонстрирует атрибуты класса и статические методы

class Critter(object):
    """ Виртуальный питомец. """

    total = 0

    @staticmethod
    def status():
        print('\nВсего зверушек сейчас', Critter.total)

    def __init__(self, name):
        print('Появилась на свет новая зверушка!')
        self.name = name
        Critter.total += 1


# основная часть
print("Нахожу значение атрибута класса Critter.total: ", end=' ')
print(Critter.total)
print("Создаю зверушек")
crit1 = Critter('зверушка 1')
crit2 = Critter('зверушка 2')
crit3 = Critter('зверушка 3')
Critter.status()
print('\nОбращаюсь к атрибуту класса через объект: ', end=' ')
print(crit1.total)
print("Нахожу значение атрибута класса Critter.total: ", end=' ')
print(Critter.total)
input("\n\nНажмите Enter, чтобы выйти.")
