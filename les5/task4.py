# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

translator = {'One': 'Один', 'Two': 'Два',
              'Three': 'Три', 'Four': 'Четыре'}

try:
    new_txt = []
    with open('task4.txt', 'r', encoding='utf-8') as file_txt:

        for line in file_txt:
            line = line.split(' - ')

            if line[0] in translator:
                new_txt.append(translator[line[0]] + ' - ' + line[1])

        print(new_txt)

except IOError:
    print("IOError")
    exit(1)

try:
    with open('task4_new.txt', 'w', encoding='utf-8') as file_txt:
        file_txt.writelines(new_txt)

except IOError:
    print("IOError")
    exit(2)
