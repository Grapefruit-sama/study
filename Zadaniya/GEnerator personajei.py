# программа "Генератор персонажей"
# Пользователь расспределяет 30 очков по 4ем характеристикам
# Реализовать функцию возврата очков обратно в пулл

points = 30
basic_statistics = {'Сила': '0',
                    'Здоровье': '0',
                    'Мудрость': '0',
                    'Ловкость': '0', }
choice = None

while choice != '0':
    print('''
    Переводчик с гикского на русский
    0 - Выйти
    1 - Распределить очки
    2 - Сбросить все характеристики
    ''')

    # Если привышен лимит очков
    if points < 0:
        print('''Вы не можете создать персанажа который
                привышает лимит доступнах очков!!''')
        points *= -1
        print(f'Лимит привышен на {points} очков.')
        print('Пожайлуста перераспределите характеристики.')
    else:
        pass

    choice = input('Что вы собираетесь сделать? ')
    print()

    # Выход
    if choice == '0':
        print('До свидания.')

    # Распределение очков
    elif choice == '1':
        ability = input('Какую характеристику изменить? ')
        # Если указанная характеристика существует а очки не меньше 0
        if ability in basic_statistics and points > 0:
            print(f'У вас {points} очков')
            scores = input('\nСколько очков вы хотите добавить? ')
            point = basic_statistics[ability]
            basic_statistics[ability] = point + scores
            points -= scores
        # Если привышен лимит очков
        elif points < 0:
            points *= -1
            print('Сумма очков не должна быть выше 30!!')
            print(f'Вы привысили лимит на {points} очков!!!!')
            print('Вы должны убрать очки из характеристик пока их сумма не'\
                  'будет равна 30!')
            scores = input('\nСколько очков вы хотите добавить? ')
            point = basic_statistics[ability]
            basic_statistics[ability] = point + scores
            points -= scores
        else:
            print('Такой характеристики не существует')
