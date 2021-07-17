# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

import sys

try:
    with open('task2.txt') as file_txt:
        lines = [line for line in file_txt.readlines() if line != '\n']

except IOError:
    print("IOError")
    sys.exit(1)

print(f"В файле непустых строк:", len(lines))

i = 1
for line in lines:
    print(f'строка {i} {line.split()} содержит {len(line.split())} слов')
    i += 1
