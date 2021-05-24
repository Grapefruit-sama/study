# Глава 5
# Списки и словари
# Игра "Рекорды"

# Программа "Рекорды"
# Демонстрирует списочные методы
scores = []
choice = None

# Отображение меню
while choice != '0':
    print(
        '''
        0 - Выйти
        1 - Показать рекорд
        2 - Добавить рекорд
        3 - Удалить рекорд
        4 - Сортировать список
        '''
        )
    choice = input('Ваш выбор: ')
    print()

    # Выход их программы
    if choice == '0':
        print('До свидания.')

    # Вывод результатов на экран
    elif choice == "1":
        print('Рекорды')
        for score in scores:
            print(score)

    # Добавление рекорда
    elif choice == '2':
        score = int(input('Введите свой рекорд: '))
        scores.append(score)

    # Удаление рекорда
    elif choice == '3':
        score = int(input('Какой из рекордов удалить?: '))
        if score in scores:
            scores.remove(score)
        else:
            print(f'Результат {score} не содежится в списке рекордов')

    # Сортировка рекордов
    elif choice == '4':
        scores.sort(reverse=True)

    # Непонятный пользовательский ввод
    else:
        print(f'Извините, в меню нет пункта {choice}')

# Конец программы
input("\nНажмите Enter. чтобы выйти.")
