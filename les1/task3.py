# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

while True:
    n = input("Введите число n >>>")
    if n.isdigit():
        n = int(n)
        break

    print('Ошибка ввода, введите число')

nn = n * 10 + n
nnn = n * 100 + n * 10 + n
res = n + nn + nnn

print(f"{n} + {nn} + {nnn} = {res}")
