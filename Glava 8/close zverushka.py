# Программа "Закрытая зверушка"
# Демонстрирует закрытые переменные и методы

class Critter(object):
    """ Втуальный питомец"""
    def __init__(self, name, mood):
        print('На свет появилась новая зверушка!')
        self.name = name  # открытый атрибут
        self.__mood = mood  # Закрытый атрибут

    def talk(self):
        print('\nМеня зовут ', self.name)
        print('Сейчас я чувствую себя', self.__mood, '\n')

    def __private_method(self):
        print('Это закрытый метод')

    def public_method(self):
        print("Это открытый метод")
        self.__private_method()


# Основная часть
crit = Critter(name='Бобик', mood='прекрасно')
crit.talk()
crit.public_method()
input('выйти')
