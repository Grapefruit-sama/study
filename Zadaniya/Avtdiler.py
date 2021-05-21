# Программа "Автодиллер"
# Глава 2 Задание 4
# Вычисляет конечную стоимоть автомобиля

stoimst = (int(input('\nВведите стоимость автомобиля без учета наценок ')))
nalg = int(stoimst * 0.2)
reg_sbor = int(stoimst * 0.15)
agent_sbor = int(60000)
tsena_dstavki = int(5000)
summ = stoimst + nalg + reg_sbor + agent_sbor + tsena_dstavki
print('\nИтоговая сумма покупки ', summ,)
input()
