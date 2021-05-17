# Программа "Монеточка"
# Подбрасывыет условну. монетку 100 раз и
# считает сколько выполо орлов а сколько решек

import random
input('Подбрасываю монетку 100 раз...')
podbrasivanii = 0
orel = 0  # Орел при значании монетки == 1
reshka = 0  # Решка при значении манетки == 2
while podbrasivanii != 100:
    monetka = random.randint(1, 2)
    podbrasivanii += 1
    if monetka == 1:
        orel += 1
    elif monetka == 2:
        reshka += 1
print('Орлов - ', orel, 'Решек - ', reshka,)
input('')
