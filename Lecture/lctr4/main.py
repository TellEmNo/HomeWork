# def f(x):
#     return x*x
#
# a = f    # a хранит в себе ссылку на функцию f
#
# print(a(3))
# print(f(5))

# def calc1(a, b):
#     return a + b
#
# def calc2(a, b):
#     return a * b
#
# def math(op, x, y):
#     print(op(x, y))
#
# math(calc1, 5, 4)
# math(calc2, 5, 4)

# def math(op, x, y):
#     print(op(x, y))

# def calc1(a, b):
#     return a + b

# или

# calc1 = lambda a, b: a + b

# или

# math(lambda a, b: a + b, 3, 7)


# В списке хранятся числа. Нужно выбрать только четные числа и составить список пар (число, квадрат числа).

# from random import randint

# list1 = [randint(0, 100) for i in range(10)]
# res = list()
#
# for item in list1:
#     if item % 2 == 0:
#         res.append((item, item**2))
#
# print(res)

# from random import randint


# def select(f, col):   # возврат всех элементов списка
#     return [f(x) for x in col]
#
# def where(f, col):    # возврат только четных элементов
#     return [x for x in col if f(x)]
#
#
# list1 = [randint(0, 100) for i in range(10)]
# res = select(int, list1)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)

# list1 = [x for x in range(1, 21)]
# print(list1)
#
# list1 = list(map(lambda x: x + 10, list1))
# print(list1)

# Задача: С клавиатуры вводится некий набор чисел, в качестве разделителя используется пробел.
# Этот набор чисел будет считан в качестве строки.
# Как превратить list строк в list чисел?

# str = '12 23 21412 4322 12 21'
# print(str)

# str = str.split()
# print(str)

# str = list(map(int, str.split()))
# print(str)

# from random import randint
#
# def where(f, col):    # возврат только четных элементов
#     return [x for x in col if f(x)]
#
#
# list1 = [randint(0, 100) for i in range(10)]
# res = map(int, list1)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)


# data = [15, 65, 9, 36, 175]
#
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)


# from random import randint
#
# list1 = [randint(0, 100) for i in range(10)]
# res = map(int, list1)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)


# Функция zip

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

# Функция zip пробегает по минимальному входящему набору:

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]

# Функция enumerate

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
#
# data = list(enumerate(users))
#
# print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3'), (3, 'user4'), (4, 'user5')]

# Работа с файлами

# colors = ['Red', 'green', 'blue']
# data = open('file.txt', 'a')  # указываем режим, в котором будем работать
# data.writelines(colors)  # разделителей не будет
# data.close()  # если мы открыли файл, то обязательно должны закрыть
#
# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')
#
# print()

path = 'file.txt'
data = open('file.txt', 'r')
for line in data:
    print(line)
data.close()