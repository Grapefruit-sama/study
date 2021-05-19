# Глава 4
# Циклы с оператором for, строки и кортежи.
# Игра "Анаграммы"

# Программа "Слово по буквам"
# Демонстрирует применение цикла for к строке
word = input('Введите слово: ')
print('\nВот все буквы вашего слова попорядку:')
for latter in word:
    print(latter)
input('\nНажмите Enter, чтобы выйти.')

# Программа "Считалка"
# Демонстрирует использование функции range()
print('Посчитаем: ')
for i in range(10):
    print(i, end=' ')
print('\nПеречислим кратные пяти: ')
for i in range(0, 51, 5):
    print(i, end=' ')
print('\nПосчитаем в обратном порядке: ')
for i in range(10, 0, -1):
    print(i, end=' ')
input("\nHaжмитe Enter. чтобы выйти.\n")

# Программа "Анализатор текста"
# Демонстрирует работу функции len() и оператора in
message = input('Введите текст: ')
print(f'Длинна введенного вами текста состовляет: {len(message)}')
print('Самая частая согласная "Т"')
if 'т' in message:
    print('Встречается в вашем тексте')
else:
    print('не встречается в вашем тексте')
input("\nHaжмитe Enter. чтобы выйти.\n")

# Программа "Случайные буквы"
# Демонстрирует индексацию строк
import random
word = "индекс"
print(f'В переменной word хранится слово: {word}')
high = len(word)
low = -len(word)
for i in range(10):
    position = random.randrange(low, high)
    print(f'word[ {position} ]\t {word[position]}')
input("\nHaжмитe Enter. чтобы выйти.\n")

# Программа "только гласные"
# демонстрирует, как созовать новые строки из исходных с помощью цикла for
message = input('Введите текст ')
new_message = ''
VOWELS = 'eyuioaуеыаоэяию'
print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print('Создана новая строка: ', new_message,)
print('\nВот ваш текст с изъятыми буквами: ', new_message)
input("\nHaжмитe Enter. чтобы выйти.\n")
