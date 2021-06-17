# Программа "Зверюшка с конструктором"
# Демонстрирует метод конструктор

class Critter(object):
    """ Виртуальный питомец. """
    def __init__(self):
        print('Появилась на свет новая зверушка!')

    def talk(self):
        print('\nПривет. Я зверюшка - экземпляр класса Critter.')


# основная часть
crit1 = Critter()
crit2 = Critter()
crit1.talk()
crit2.talk()
input("\n\nНажмите Enter, чтобы выйти.")
