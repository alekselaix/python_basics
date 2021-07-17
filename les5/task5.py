# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


user_number = "1 2 2.2 3.5 777 99.9 500"

summa = 0

try:
    with open('task5.txt', 'w', encoding='utf-8') as file_txt:
        file_txt.write(user_number)

    with open('task5.txt', encoding='utf-8') as file_txt:
        data = file_txt.read()

    try:
        for i in data.split():
            summa += float(i)
    except ValueError:
        print("ValueError")
        exit(1)


except IOError:
    print("IOError")
    exit(2)

print(summa)
