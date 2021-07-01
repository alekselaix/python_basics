# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчете на одного сотрудника

while True:
    proceeds = input("Введите значение выручки >>> ")
    if proceeds.isdigit():
        proceeds = int(proceeds)
        break

    print('Ошибка ввода, введите число')

while True:
    expenses = input("Введите количество издержек >>> ")
    if expenses.isdigit():
        expenses = int(expenses)
        break

    print('Ошибка ввода, введите число')

profit = proceeds - expenses  # Прибыль

if profit > 0:
    roi = profit / proceeds
    print(f"Прибыль компании = {profit}, Рентабельность компании = {roi}")

    while True:
        employees = input("Введите колличество сотрудников >>> ")
        if employees.isdigit():
            employees = int(employees)
            break

        print('Ошибка ввода, введите число')

    profit_employees = profit / employees
    print(f"Прибыль на одного сотрудника  = {profit_employees}")

elif profit == 0:
    print("Работа компании в 0, хотябы не в убыток")
else:
    print(f"Убыток компании = {profit}")
