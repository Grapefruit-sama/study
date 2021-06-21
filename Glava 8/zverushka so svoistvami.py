# Программа "Зверюшка со свойствами"
# Демонстрирует свойства

class Critter(object):
    """ Виртуальный питомец. """
    def __init__(self, name):
        # boilerplate
        print('Появилась на свет новая зверушка!')
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == '':
            print('Имя зверушки не может быть пустой строкой')
        else:
            self.__name = new_name
            print("Успешно изменено")

    def talk(self):
        print('\nМеня зовут ', self.name)


# основная часть
crit = Critter("Бобик")
crit.talk

print("\nМою зверюшку зовут", end=" ")
print(crit.name)

print("\nПробую изменить имя зверюшки на Мурзик...")
crit.name = "Мурзик"
print(crit.name)

print("\nПробую изменить имя зверюшки на пустую строку...")
crit.name = ""
print(crit.name)

print("Мою зверюшку зовут", end=" ")
print(crit.name)
input("\n\nНажмите Eпter, чтобы выйти.")
