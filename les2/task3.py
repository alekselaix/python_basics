# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

number_list = [(12, 1, 2), (3, 4, 5),
               (6, 7, 8), (9, 10, 11)]

season_list = ['Зима', 'Весна', 'Лето', 'Осень']

season_dict = {'Зима': (12, 1, 2), 'Весна': (3, 4, 5),
               'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}

while True:
    user_number = input('Введите месяц в виде целого числа от 1 до 12 >>>  ')
    if user_number.isdigit():
        user_number = int(user_number)
        break

    print('Ошибка ввода, введите число')

if 1 <= user_number <= 12:
    # Решение через list
    i = 0
    for elem in number_list:
        if user_number in elem:
            print(f'Решение через list\t {season_list[i]}')
            break
        i += 1

    # Решение через dict
    for key, elem in season_dict.items():
        if user_number in elem:
            print(f'Решение через dict\t {season_dict.get(elem, key)}')
            break
else:
    print(f'Месяц {user_number} не существует')
