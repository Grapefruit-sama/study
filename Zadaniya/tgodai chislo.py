# Компьютер выбирает случайное число в диапазоне от 1 до 100
# Игрок пытается отгадать это число. и компьютер говорит.
# предположение больше/меньше. чем загаданное число.
# или попало в точку

import random

from typing import (
    List,
    Union,
    NoReturn,
)


def ask_number(question: int, low: int, high: int) -> int:
    """ Просит ввести число из диапазона. """
    
    response = None
    
    while response not in range(low, high):
        response = int(input(question))
    return response



print("\tДобро пожаловать в игру 'Отгадай число'!")
print("\nЯ загадал натуральное число из диапазона от 1 до 10.")
print("Постарайтесь отгадать его за 5 попыток.\n")
# Начальные значения переменных
number = random.randint(1, 10)
guess = int(input('Ваше продположение? '))
tries = 1
# цикл отгадывания
while guess != number and tries != 5:
    if guess > number:
        print('Меньше...')
    else:
        print('Больше...')
    guess = int(input('Ваше продположение? '))
    tries += 1
if guess == number:
    print("\nBaм удалось отгадать число! Зто в самом деле", number)
    print("Bы затратили на отгадывание всего лишь ", tries, " попыток!\n")
elif tries == 5:
    print('\nУ вас закончилось количество попыток')
    print("Число было ", number)
input("\n\nНажмите Enter. ·чтобы выйти.")
