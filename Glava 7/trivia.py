# Программма "Викторина"
# Игра на выбор правильного варианта ответа
# вопросы которой читаются из текстового файла

import sys

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
    explanation = next_line(the_file)
    return category, question, answers, correct, explanation


def welcome(title: str) -> NoReturn:
    """ Приветствует игрока и сообщает тему игры. """

    print('\t\tДобро рпдаловать в игру "Викторина"!\n')
    print(f'\t\t{title}\n')


def main():
    trivia_file = open_file('Glava 7\\trivia.txt', 'r')
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    # Извлечение первого блока
    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print(f'\t {i + 1} - {answers[i]}')
        # Получение ответа
        answer = input("Ваш ответ: ")
        # проверка ответа
        if answer == correct:
            print("\nДа!", end=" ")
            score += 1
        else:
            print("\nНет не верно", end=" ")
        print(explanation)
        print(f'Счет {score} \n\n')
        # переход к следующему вопросу
        category, question, answers, correct, explanation = next_block(trivia_file)
    trivia_file.close()
    print('Это был последний вопрос!')
    print('На вашем счету', score)


main()
input('\n\nНажмите Enter чтобы выйти')
