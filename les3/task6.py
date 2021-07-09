# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().\

def int_func(text):
    """
    Программа меняет нижний регистр слова на верхний
    'text text' -> 'Text Text'
    :param text:строка из латинских букв нижнего регистра
    :return:строка, слова в которой начинается с верхнего регитсра
    """
    return text.title()


print(int_func('text'))
print(int_func('text text'))
print(int_func('Hello world 123 print text'))


def int_func1(text_data):
    """
    Программа меняет нижний регистр слова на верхний
    'text text' -> 'Text Text'
    :param text_data:строка из латинских букв нижнего регистра
    :return:строка, слова в которой начинается с верхнего регитсра
    """
    list_data = []

    for word in text_data.split():
        list_data.append(word[0].upper() + word[1:])

    return list_data


print(int_func1('text'))
print(int_func1('text text'))
print(int_func1('Hello world 123 print text'))
