# c = 5.89
# print(c)
# print(type(c))
# c = int(c)
# print(c)
# print(type(c))
# c = str(c)
# print(c + 'd323')
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))


# print('Введите первое число: ')
# n = int(input())
# m = float(input('Введите второе число: '))

# print(f"{n} + {m} = {n + m}")


# a = 5.432
# b = 2.353446
# # округление
# print(round(a * b, 1))


# username = input('Введите ваше имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Влад':
#     print('Ура, это же Влад!')
# elif username == 'Владимир':
#     print('Владимир Владимирович, это Вы?')
# else:
#     print(f'Ну, здарова, {username}')


# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0:  # Если остаток от деления числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2:  # Делитель числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1


# for i in range(0, 23, 3): # 3 - это шаг, если его убрать совсем, то по умолчанию шаг = 1
#     print(i)


# a = 'qwerty'

# for i in a:
#     print(i)


# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)


text = 'Съешь еще этих мягких французских булочек'

# .lower - перевод строки в нижний регистр
# .upper - перевод строки в верхний регистр
# .replace('ещё','ЕЩЁ') - замена, первый аргумент - что меняем, второй - на что меняем

print(text[len(text)])
