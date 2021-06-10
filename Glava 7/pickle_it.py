# Программа "Законсервируем"
# Демонстрирует консервацию данных и доступ к ним через интерфейс полки

import pickle
import shelve

print('консервация списков')
variety = ['огурцы', 'помидоры', 'капуста', ]
shape = ['целые', 'кубиками', 'соломкой', ]
brand = ['Главпродукт', 'Чумак', 'Бондюэль', ]

f = open('Glava 7\\pickles1.dat', 'wb')
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print('\nреконсервация списков')
f = open('Glava 7\\pickles1.dat', 'rb')
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)
print(variety)
print(shape)
print(brand)
f.close()

print('\nПомещение списков на полку')
s = shelve.open('Glava 7\\pickles2.dat')
s['variety'] = ['огурцы', 'помидоры', 'капуста', ]
s['shape'] = ['целые', 'кубиками', 'соломкой', ]
s['brand'] = ['Главпродукт', 'Чумак', 'Бондюэль', ]
s.sync()  # убедимся что данные записаны

print('\nИзвлечение списков из файла полки')
print('Торговые марки - ', s['brand'])
print('Формы - ', s['shape'])
print('виды овощей - ', s['variety'])
s.close()

input('Выход')
