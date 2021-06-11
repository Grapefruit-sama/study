# Программа "Обработаем"
# Демонстрирует обработку исключительных ситуаций
# try/except

try:
    num = float(input('Введите число: '))
except:
    print("Похоже это не число!")


# обработка исключения определенного типа
try:
    num = float(input("\nBвeдитe число: "))
except ValueError:
    print("Этo не число!")

# Обработка исключений нескольких разных типов
print()
for value in (None, 'Привет!'):
    try:
        print(f'Пытаюсь преобразовать в число {value} -->', end='')
        print(float(value))
    except (TypeError, ValueError):
        print("Этo не число!")

print()
for value in (None, 'Привет!'):
    try:
        print(f'Пытаюсь преобразовать в число {value} -->', end='')
        print(float(value))
    except (TypeError):
        print("я умею преобразовывать только строки и числа")
    except (ValueError):
        print("я умею преобразовывать только строки,составленные из цифр")

# получение аргумента
try:
    num = float(input("\nBвeдитe число: "))
except ValueError as e:
    print("Этo не число! Интерпретатор как бы говорит нам: ")
    print(e)

# try/except/else
try:
    num = float(input("\nBвeдитe число: "))
except ValueError:
    print("Этo не число!")
else:
    print('Вы ввели число ', num)

input('\nНажмите Enter чтобы выйти')
