# Компьютер выбирает случайное число в диапазоне от 1 до 100
# Игрок пытается отгадать это число. и компьютер говорит.
# предположение больше/меньше. чем загаданное число.
# или попало в точку

import random
from typing import (
    NoReturn,
)


def ask_number(question: str, low: int, high: int) -> int:
    """ Просит угадать число.

    Аргументы
    ---------
    `low`: int
        нижняя граница диапазона.
    `high`: int
        верхняя граница диапазона.
    """

    guess = low - 1
    while guess not in range(low, high):
        guess = int(input(question))
    return guess


def display_instruct() -> NoReturn:
    """ Выводит на экран инструкцию для игрока. """

    print("\n\tДобро пожаловать в игру 'Отгадай число'!\n")
    print("\tЯ загадал натуральное число из диапазона от 1 до 100.")


def guess_loop(guess: int, number: int) -> int:
    """ Проверяет ввод игрока. """

    # цикл отгадывания
    while guess != number:

        if guess > number:
            print('Меньше...')
        else:
            print('Больше...')

        guess = ask_number('Ваше продположение?', 0, 100)
    return guess


def congrat(guess: int, number: int) -> NoReturn:
    """ Вывод победы. """
    if guess == number:
        print("\nBaм удалось отгадать число! Зто в самом деле", number)


def main():
    # Начальные значения переменных
    number = random.randint(1, 100)

    display_instruct()
    guess = ask_number('Ваше продположение? ', 0, 100)
    guess = guess_loop(guess, number)
    congrat(guess, number)


main()
input("\n\nНажмите Enter. ·чтобы выйти.")
