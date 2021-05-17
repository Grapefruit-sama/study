# Программа "Сюрприз"
# Отображает один из вариантов сюрприза

import random
print('Вы берете пирожек из корзинки.')
input('Интересно с чем же он?\n')
nachinka = random.randint(1, 5)
if nachinka == 1:
    print('кажется это клубника')
elif nachinka == 2:
    print('Горячее! Яблочное повидло.')
elif nachinka == 3:
    print('Какое кислое. Черника...')
elif nachinka == 4:
    print('Мммм капуста')
elif nachinka == 5:
    print('Феее яйцо с луком')
else:
    print('Хуй те а не пирожок')
input('\nВыйти')
