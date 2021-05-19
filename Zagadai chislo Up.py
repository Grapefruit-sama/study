# Программа "Загадай число"
# Игрок загадывает компьютеру число в заданном диапазоне
# Компьютер пытается его отгодать

import random
print("\tДобро пожаловать в игру 'Загадай число'!")
print("\nЗагадай натуральное число из диапазона от 1 до 100.")
print("Я постараюсь отгадать его!!!!")
print("Я буду говорить варианты, а ты просто говори 'да' или 'нет'")
print("У меня всего 5 попыток!\n")

# Начальные значения переменных
otvet = 'нет'
number_min, number_max = 1, 100
number_curr = random.randint(number_min, number_max)
tries = 0

# цикл отгадывания
while otvet != "да" and tries < 5:
    print(number_curr, '?')
    otvet = input('Верно? ')

    # Изменяет ренж рандомайзера
    if otvet == 'больше':
        number_min = number_curr + 1
        number_curr = random.randint(number_min, number_max)
        tries += 1

    # Изменяет ренж рандомайзера
    elif otvet == 'меньше':
        number_max = number_curr - 1
        number_curr = random.randint(number_min, number_max)
        tries += 1

    # Завершение цикла
    elif otvet == 'да':
        break

    # В иных случаях
    else:
        number_curr = random.randint(number_min, number_max)
        tries += 1

if otvet == "да":
    print("\nМне удалось отгадать число!")
    print(f"Я затратил на отгадывание всего лишь {tries} попыток!\n")
else:
    print('\nУ меня закончилось количество попыток')
    print("В следущий раз повезет")

input("\n\nНажмите Enter. ·чтобы выйти.")
