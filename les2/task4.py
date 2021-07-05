# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

# user_data = ["Здесьбольшечемдесятьсимволов", "123", "Привет", "МирТрудМай"]

user_data = input("Введите строку из нескольких слов >>> ")
user_data = user_data.split()

if user_data != " ":
    i = 0
    for elem in user_data:
        if len(elem) > 10:
            print(f"{i}\t{elem[0:10]}")
        else:
            print(f"{i}\t{elem}")
        i += 1
    else:
        print(f"{i}\tПробел")

# более сложный для понимания варинат
# user_word = []
# i = 0
#
# for elem in range(user_data.count(" ") + 1):
#
#     user_word = user_data.split()
#
#     if len(str(user_word)) > 10:
#         print(f"{i}\t{user_word[i][0:10]}")
#
#     else:
#         print(f"{i}\t{user_word[i]}")
#     i += 1
