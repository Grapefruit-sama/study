# Глава 4 продолжение
# Циклы с оператором for, строки и кортежи.
# Игра "Анаграммы"

# Программа " Резчик пиццы"
# демонстрирует срезы строк
word = 'пицца'
print(
    '''
0   1   2   3   4   5
+---+---+---+---+---+
| п | и | ц | ц | а |
+---+---+---+---+---+
-5  -4  -3  -2  -1
''')
print(
    "Введите начальный и конечный индексы для того среза 'пиццы'"\
    "который хотите получить."
     )
print('Нажмите Enter, не вводя начальную позицию')
start = None
while start != "":
    start = (input('Начальная позиция: '))
    if start:
        start = int(start)
        finish = int(input('Конечная позиция: '))
        print(f"Срез word[{start}]:[{finish}] выглядит как.", end=' ')
        print(word[start:finish])
input("\nHaжмитe Enter. чтобы продолжить.\n")

# Программа "Арсенал героя"
# Демонстрирует создание кортежа
# Создадим пустой картеж
inventory = ()
# рассмотрим его как условие
if not inventory:
    print('Вы безоружны')
input("\nHaжмитe Enter. чтобы продолжить.\n")
# Теперь создадим кортеж с несколькими элементами
inventory = (
    'меч',
    'кольчуга',
    'щит',
    'целебное снадобье',
)
# Выведем этот кортеж на экран
print('Содержимое кортежа: ')
print(inventory)
# Выведем все элементы последовательно
print('\nИ так в вашем арсенале: ')
for item in inventory:
    print(item)
input("\nHaжмитe Enter. чтобы продолжить.\n")

# Программа "Арсенал героя 2"
# Демонстрирует работу кортежа
# Создадим картеж с несколькими элементами
# и выведеме его с помощью цикла for
inventory = (
    'меч',
    'кольчуга',
    'щит',
    'целебное снадобье',
)
print('\nИтак, в вашем арсенале: ')
for item in inventory:
    print(item)
input("\nHaжмитe Enter. чтобы продолжить.\n")
# Длинна кортежа
print(f'Сейчас в вашем распоряжении {len(inventory)} предмета/-ов')
input("\nHaжмитe Enter. чтобы продолжить.\n")
# проверка на принадлежность кортежу с помощью in
if "целебное снадобье" in inventory:
    print("Вы еще поживете и повоюете.")
# вывод одного элемента с определенным индексом
index = int(input('\nВведите индекс одного из предметов арсенала: '))
print(f'Под индексом {index} в арсенале находится {inventory[index]}')
# отобразим срез
start_1 = int(input('\nВедите начальный индекс среза: '))
finish_1 = int(input('\nВедите конечный индекс среза: '))
print(f'Срез inventory[{start_1}:{finish_1}]- это', end=' ')
print(inventory[start_1:finish_1])
input("\nHaжмитe Enter. чтобы продолжить.\n")
# Соеденим 2 кортежа
chest = ('золото', 'драгоценные камни', )
print('Вы нашли ларец. Вот что в нем есть: ')
print(chest)
print('Вы забираете содержимое')
inventory += chest
print('Теперь в вашем распоряжении: ')
print(inventory)
input("\nHaжмитe Enter. чтобы выйти.\n")
