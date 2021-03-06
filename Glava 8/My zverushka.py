# Программа "Моя зверушка"
# Виртуальный питомец, о котором пользователь может заботится

class Critter(object):
    """ Виртуальный питомецю. """
    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 10 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print(f'Меня зовут {self.name} и сейчас я чувствую себя {self.mood}\n')
        self.__pass_time()

    def eat(self, food=4):
        print('Мрр... Спасибо!')
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print('Уиии!')
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    crit_name = input("Как вы назовете свою зверушку? ")
    crit = Critter(crit_name)

    # меню
    choice = None
    while choice != '0':
        print("""
                Моя зверушка
                0 - Выйти
                1 - Узнать о самочувствии зверушки
                2 - Покормить зверушку
                3 - Поиграть со зверушкой
        """)
        choice = input('Ваш выбор: ')
        print()
        # Выход
        if choice == '0':
            print("До свидания")

        # беседа со зверушкой
        elif choice == "1":
            crit.talk()

        # кормление зверушки
        elif choice == "2":
            crit.eat()

        # игра со зверушкой
        elif choice == "3":
            crit.play()

        # непонятный пользовательский ввод
        else:
            print('Изнините в меню нет такого пункта')


main()
input('\n\nНажмите ВВод чтобы выйти')
