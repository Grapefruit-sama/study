# Программма "Викторина"
# Игра на выбор правильного варианта ответа
# вопросы которой читаются из текстового файла

import sys
import pickle

from typing import (
    NoReturn,
    IO,
    Union,
)


def open_file(file_name: str, mode: str) -> IO:
    """ Открывает файл. """

    try:
        the_file = open(file_name, mode, encoding='utf-8')
    except IOError as e:
        print(f'Невозмжно открыть файл {file_name}. Работа программы будет завершена.\n {e}')
        input('\nНажмите Enter чтобы выйти')
        sys.exit()
    else:
        return the_file


def next_line(the_file: IO) -> str:
    """ Возвращает отформатированном виде очередную строку игрового файла. """

    line = the_file.readline()
    line = line.replace('/', '\n')
    return line


def next_block(the_file: IO) -> Union[str, list]:
    """ Возвращает очередной блок данных из игрового файла. """

    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    denomination = next_line(the_file)
    explanation = next_line(the_file)
    return category, question, answers, correct, denomination, explanation


def par(denomination: str) -> int:
    """ Переводит строку `denomination` в int. """

    digit = '1234567890'
    point = ''
    for number in denomination:
        if number in digit:
            point += number
    point = int(point)
    return point


def welcome(title: str) -> NoReturn:
    """ Приветствует игрока и сообщает тему игры. """

    print('\t\tДобро рпдаловать в игру "Викторина"!\n')
    print(f'\t\t{title}\n')


def write_record(score: int) -> NoReturn:
    """ Записывает рекорд с именем и очками в файл. """

    name = input('Введите имя: ')
    
    score = str(score)
    record = name + ' ' + score + '\n'
    record_list = open('Glava 7\\record_list.txt', 'a+')
    record_list.write(record)
    record_list.close()


def display_record() -> NoReturn:
    """ Отображает список рекордов из файла"""
    record_list = open('Glava 7\\record_list.txt', 'r')
    print(record_list.read())
    record_list.close()


def main():
    trivia_file = open_file('Glava 7\\trivia.txt', 'r')
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    # Извлечение первого блока
    category, question, answers, correct, denomination, explanation = next_block(trivia_file)
    while category:
        print(category)
        print(question)
        print('Вопрос наминалом в :', denomination)
        for i in range(4):
            print(f'\t {i + 1} - {answers[i]}')
        # Получение ответа
        answer = input("Ваш ответ: ")
        # проверка ответа
        if answer == correct:
            print("\nДа!", end=" ")
            score += par(denomination)
        else:
            print("\nНет не верно", end=" ")
        print(explanation)
        print(f'Счет {score} \n\n')
        # переход к следующему вопросу
        category, question, answers, correct, denomination, explanation = next_block(trivia_file)
    trivia_file.close()
    print('Это был последний вопрос!')
    print('На вашем счету', score)
    y_or_n = input('Хотите ли вы записать рекорд? (y/n): ')
    if y_or_n == 'y':
        write_record(score)
    else:
        pass
    y_or_n = input('Хотите ли вы посмотреть список рекордов? (y/n): ')
    if y_or_n == 'y':
        display_record()
    else:
        pass


main()
input('\n\nНажмите Enter чтобы выйти')
