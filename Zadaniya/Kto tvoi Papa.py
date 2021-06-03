# Программа "Кто твой папа?"
# Пользователь вводит им человека а программа называет отца этого человека
# Так же предоставляется возможность добавлять,
# заменять и удалять пары «СЫН - отец»

# Переменные
family = {'Саня': 'Федор Анатольевич',
          'Джорно': 'Михаил Петрович',
          'Мордред': 'Артур Утерович',
          'Федя': 'Иван Ибрагимович',
          'Камил': 'Азим Колымбекович',
          'Артур Утерович': 'Тор Одинович',
          'Иван Ибрагимович': 'Тор Одинович',
          'Азим Колымбекович': 'Карна Сансарович', }
choice = None
while choice != 0:
    print('''
    Сын-Отец
    0 - Выйти
    1 - Найти папу
    2 - Добавить семью
    3 - Изменить семью
    4 - Удалить семью
    ''')
    choice = int(input('Ваш выбор: '))
    print()
    # Выход
    if choice == 0:
        print('До свидания.')

    # поиск толкования
    elif choice == 1:
        son = input('Отца какого человека вы хотите узнать? ')
        if son in family:
            father = family[son]
            print(f'\n Отец {son} - {father}')
            if father in family:
                grandfather = family[father]
                print(f'\n Дед {son} - {grandfather}')
            else:
                pass
        else:
            print('\nУвы этот человек мне не знаком')

    # Добовление семь
    elif choice == 2:
        son = input('Кого вы хотите добвить? ')
        if son not in family:
            father = input('\nВпишите его отца ')
            family[son] = father
            print(f'\nСемья {son} добавлена в словарь')
        else:
            print('\nТакая семья уже есть в словаре')

    # изменение значения в словаре
    elif choice == 3:
        son = input('Чьего отца вы хотите изменить? ')
        if son in family:
            father = input('\nВпишите отца')
            family[son] = father
            print(f'\nСемейная связь с {son} изменена')
        else:
            print('\nТакого человека пока нет!')

    # удаление термина
    elif choice == 4:
        son = input('Чью семью вы хотите удалить? ')
        if son in family:
            del family[son]
            print(f'\nСемья {son} удаленв')
        else:
            print('\nТакой семьи пока нет!')

    # Непонятный пользовательский ввод
    else:
        print(f'Извините, в меню нет пункта {choice}')

# Конец программы
input("\nНажмите Enter. чтобы выйти.")
