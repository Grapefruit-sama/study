# Программа "Слова"
# Программа выводит спосок слов в случайном пордке

import random
# Переменные
WORDS = ('говно', 'залупа', 'пенис', 'хер', 'давалка',  # Список слов
         'хуй', 'головка', 'шлюха', 'жопа', 'член', 'еблан',
         'петух', 'рукоблуд', 'ссанина', 'очко', 'блядун', 'вагина',)
positions = []
jumble = ''
position = None
for i in WORDS:
    position = random.randrange(len(WORDS))
    # position = str
    if position not in positions:
        positions = int(positions) + int(position)
        jumble = WORDS[position]
        jumble = jumble[:position] + jumble[(position+1):]
        print(jumble)
    else:
        pass
