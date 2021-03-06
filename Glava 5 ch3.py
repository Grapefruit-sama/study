# Глава 5 часть 3
# Списки и словари
# Игра "Рекорды 2.0"

# Программа "Рекорды 2.0"
# Демонстрирует вложенные последовательности
scores = []
choice = None

# Отображение меню
while choice != '0':
    print(
        '''
        Рекорды 2.0
        0 - Выйти
        1 - Показать рекорд
        2 - Добавить рекорд
        '''
        )
    choice = input('Ваш выбор: ')
    print()

    # Выход их программы
    if choice == '0':
        print('До свидания.')

    # Вывод результатов на экран
    elif choice == "1":
        print('Рекорды\n')
        print('ИМЯ\tРЕЗУЛЬТАТ')
        for entry in scores:
            score, name = entry
            print(name, '\t', score)

    # Добавление рекорда
    elif choice == '2':
        name = input('Впешите имя игрока: ')
        score = int(input('Введите его рекорд: '))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]  # Только 5 рекордов для списка

    # Непонятный пользовательский ввод
    else:
        print(f'Извините, в меню нет пункта {choice}')

# Конец программы
input("\nНажмите Enter. чтобы выйти.")


# Переводчик с гикского на русский
# Демонстрирует использование словарей
geek = {'404': 'Не знать, не владеть информацией. От сообщения об ошибке 404\
         "Страница не найдена".',
        'Googlong': '"Гугление"- поиск в Сети сведений о чем-либо',
        'Keyboard Plaque': 'Мусор который скапливается в клавиатуре компьютера',
        'Link Rot': 'Процесс устаривание гиперссылок на веб-страницах',
        'Percussive Maintenance': 'О ситуации когда кто-либо бьет по корпусу\
         неисправного электроприбора в надежде восстановить его работу',
        'Uninstalled': 'Об увольнении кого-либо. Особенно популярно\
        на рубеже 1990-2000-х годов', }

# Доступ к значению по ключу
geek['404']

# Проверка существования ключа с помощью оперетора in
if 'irgjeorig;o' in geek:
    print('Я знаю что это')
else:
    print('Я понятия не имею что это такое')

# Доступ к значениям с помощью метода get()
print(geek.get('Dancing Baloney', 'Понятия не имею'))

choice = None
while choice != '0':
    print('''
    Переводчик с гикского на русский
    0 - Выйти
    1 - Найти толкование термина
    2 - Добавить термин
    3 - Изменить толкование
    4 - Удалить термин
    ''')
    choice = input('Ваш выбор: ')
    print()
    # Выход
    if choice == '0':
        print('До свидания.')

    # поиск толкования
    elif choice == '1':
        term = input('Какой термин вы хотите перевести с гикского на русский? ')
        if term in geek:
            definition = geek[term]
            print(f'\n {term} означает {definition}')
        else:
            print('\nУвы этот термин мне не знаком')

    # Добовление термина с тлкованием
    elif choice == '2':
        term = input('Какой термин гикского языка вы хотите добавить? ')
        if term not in geek:
            definition = input('\nВпишите ваше толкование')
            geek[term] = definition
            print(f'\nТермин {term} добавлен в словарь')
        else:
            print('\nТакой термин уже есть в словаре')

    # изменение значения в словаре
    elif choice == '3':
        term = input('Какой термин гикского языка вы хотите изменить? ')
        if term in geek:
            definition = input('\nВпишите ваше толкование')
            geek[term] = definition
            print(f'\nТермин {term} изменен')
        else:
            print('\nТакого термина пока нет!')

    # удаление термина
    elif choice == '4':
        term = input('Какой термин гикского языка вы хотите удалить? ')
        if term in geek:
            del geek[term]
            print(f'\nТермин {term} удален')
        else:
            print('\nТакого термина пока нет!')

    # Непонятный пользовательский ввод
    else:
        print(f'Извините, в меню нет пункта {choice}')

# Конец программы
input("\nНажмите Enter. чтобы выйти.")
