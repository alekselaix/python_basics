# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

import sys

try:
    with open('task3.txt', encoding='utf-8') as file_txt:
        employees = file_txt.readlines()

except IOError:
    print("IOError")
    sys.exit(1)

summa_salary = 0

for employee in employees:
    name, salary = employee.split()

    try:
        salary = float(salary)
    except ValueError:
        continue

    summa_salary += salary
    if salary < 20000:  # оклад менее 20т.
        print(name)

print("Средняя зп. сотрудника: ", round(summa_salary / len(employees), 2))
