# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

goods = []
while input("Добовить товар? Ведите yes/no >>> ") == 'yes':

    number = int(input("Введите номер товара >>> "))

    user_data = {}

    while input('Добаваить параметры товара? Введите yes/no >>> ') == 'yes':
        key = input('Введите наименование параметра товара >>> ')
        value = input('Введите значение параметра товара >>> ')
        user_data[key] = value
    goods.append(tuple([number, user_data]))
print(goods)


# goods = [(1, {'name': 'computer', 'price': '10', 'num': '5', 'unit': 'pc.'}),
#           (2, {'name': 'server', 'price': '100', 'num': '2', 'unit': 'pc.'}),
#           (3, {'name': 'router', 'price': '30', 'num': '1', 'unit': 'pc.'}),
#           (4, {'name': 'printer', 'price': '15', 'num': '2', 'unit': 'pc.'})]

analytics = {}  # словарь с данными аналитики

for elem in goods:
    for key, value in elem[1].items():
        if key in analytics:
            analytics[key].append(value)
        else:
            analytics[key] = [value]
print(analytics)
