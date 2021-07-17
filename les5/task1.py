# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

user_list = []

while True:
    user_list = input('Введите строку >>> ')
    if not user_list:
        break

    try:
        with open('task1.txt', 'a') as file_text:
            file_text.write(f'{user_list}\n')
    except IOError:
        print("IOError")
        break
