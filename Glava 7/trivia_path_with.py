# Программма "Викторина"
# Игра на выбор правильного варианта ответа
# вопросы которой читаются из текстового файла

import sys

from pathlib import Path

from typing import (
    NoReturn,
    IO,
    Union,
)


def open_file(file_path: Path, mode: str) -> IO:
    """ Открывает файл. """

    # Проверка существует ли файл
    if file_path.is_file():
        the_file = open(file_path, mode, encoding='utf-8')
        return the_file
    # Если файла не существует
    elif not file_path.is_file():
        print(f'Невозмжно открыть файл {file_path}. Работа программы будет завершена.\n')
        input('\nНажмите Enter чтобы выйти')
        sys.exit()


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

    # получение вариантов ответа из файла
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)

    # проверка. После того как correct становится пустой строкой main() завершает игру
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

    # Ввод имени
    name = input('Введите имя: \n')

    # Запись имени и результата викторины в файл
    score = str(score)
    record = name + ' ' + score + '\n'
    with open(Path("Glava 7", "record_list.txt"), 'a+') as record_list:
        record_list.write(record)


def display_record() -> NoReturn:
    """ Отображает список рекордов из файла"""

    with open(Path("Glava 7", "record_list.txt"), 'r') as record_list:
        print(record_list.read())


def main():
    with open_file(Path("Glava 7", "trivia.txt"), 'r') as trivia_file:
        title = next_line(trivia_file)
        welcome(title)
        score = 0

        # Извлечение первого блока
        category, question, answers, correct, denomination, explanation = next_block(trivia_file)
        while category:
            # Вывод строк
            print(category)
            print(question)
            print('Вопрос наминалом в :', denomination)

            # Отображение вариантов ответа
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

            # Вывод после ответа
            print(explanation)
            print(f'Счет {score} \n\n')

            # переход к следующему вопросу
            category, question, answers, correct, denomination, explanation = next_block(trivia_file)

    # Уведомление об окончании виктарины
    print('Это был последний вопрос!')
    print('На вашем счету', score)

    # Запись рекордов
    y_or_n = input('Хотите ли вы записать рекорд? (y/n): ')
    if y_or_n == 'y':
        write_record(score)
    else:
        pass

    # Просмотр таблицы рекордов
    y_or_n = input('Хотите ли вы посмотреть список рекордов? (y/n): \n')
    if y_or_n == 'y':
        display_record()
    else:
        pass


main()
input('\n\nНажмите Enter чтобы выйти')
