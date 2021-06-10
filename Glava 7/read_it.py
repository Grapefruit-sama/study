# Программа"Порчитаем"
# Демонстрирует чтение текстового файла

print("Открываю и закрываю файл")
text_file = open('D:\\gitfork\\study\\Glava 7\\text.txt', 'r', encoding='utf-8')
text_file.close()

print('\nЧитаю файл посимвольно')
text_file = open('D:\\gitfork\\study\\Glava 7\\text.txt', 'r', encoding='utf-8')
print(text_file.read(1))
print(text_file.read(5))
text_file.close()

print('\nЧитаю файл целиком')
text_file = open('D:\\gitfork\\study\\Glava 7\\text.txt', 'r', encoding='utf-8')
whole_thing = text_file.read()
whole_thing = text_file.read()
print(whole_thing)
text_file.close()

print('\nЧитаю строку посимвольно')
text_file = open('D:\\gitfork\\study\\Glava 7\\text.txt', 'r', encoding='utf-8')
print(text_file.readline(1))
print(text_file.readline(5))
text_file.close()

print('\nЧитаем 1 строку целиком')
text_file = open('D:\\gitfork\\study\\Glava 7\\text.txt', 'r', encoding='utf-8')
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

print('\nЧитаю весь файл в список')
text_file = open('D:\\gitfork\\study\\Glava 7\\text.txt', 'r', encoding='utf-8')
lines = text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)
text_file.close()

print('\nПерербираю весь файл построчно')
text_file = open('D:\\gitfork\\study\\Glava 7\\text.txt', 'r', encoding='utf-8')
for line in text_file:
    print(line)
text_file.close()

input()
