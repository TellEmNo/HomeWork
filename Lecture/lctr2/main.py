# list_1 = [] # Создание пустого списка
# list_2 = list() # Создание пустого списка
# list_1 = [7, 9, 11, 13, 15, 17]
#
# print(list_1[0]) # 7
#
# print(*list_1)

# for i in list_1:
#     print(i, end=" ")
#
# print(f"\n{len(list_1)}")

# list_1 = []
# for i in range(5):
#     list_1.append(i)
# print(list_1)

# Удаление последнего элемента списка:
#
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) # 0
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]

# Удаление конкретного элемента из списка:

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12
# print(list_1) # [7, -1, 21, 0]

# Добавление элемента на нужную позицию:

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 666))
# print(list_1) # [12, 7, 666, -1, 21, 0]

# Срезы:

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(list_1[0])                 # 1
# print(list_1[-1])                # 10
# print(list_1[-5])                # 6
# print(list_1[:])                 # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# print(list_1[:2])                # 1, 2
# print(list_1[len(list_1) - 2:])  # 9, 10
# print(list_1[2:9])               # 3, 4, 5, 6, 7, 8, 9
# print(list_1[0: len(list_1): 6]) # 1, 7
# print(list_1[::6])               # 1, 7

# Кортежи:

# t = ()  # создание пустого кортежа
# print(type(t))  # class <'tuple'>
#
# t = (1,)
# print(type(t))
#
# t = (1)
# print(type(t))
#
# v = [1, 2, 3]
# print(v)  # [1, 2, 3]
# print(type(v))  # <class 'list'>
#
# v = tuple(v)
# print(v)  # (1, 2, 3)
# print(type(v))  # <class 'tuple'>
#
# a, b = 1, 2  # просто фишка
#
# a = b = 1  # ещё одна просто фишка
#
# a, b, c = v
#
# print(a, b, c)

# t = (1, 2, 3, 5)
#
# print(t[1])  # вывод элемента кортежа
#
# for i in t:
#     print(i, end=" ")  # вывод элементов кортежа через цикл
#
# print()
#
# for i in range(len(t)):
#     print(t[i], end=" ")  # можно выводить элементы так, это б

# Словари

# dictionary = {}  # Пустой словарь

# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary)  # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary['left'])  # ← типы ключей могут отличаться
# print(dictionary['up'])  # ↑ типы ключей могут отличаться
# dictionary['left'] = '<='
# print(dictionary['left'])  # <=
# print(dictionary['type'])  # KeyError: 'type'
# del dictionary['left']

# dictionary[88] = 88005553535

# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item]))  # Вывод {ключ}: {значение}

# for (k, v) in dictionary.items():
#     print(k, v)  # Вывод ключ значение

# print(dictionary.items())  # Вывод словаря, где каждый элемент элемент выводится кортежем, типа ('ключ', 'значение')

# Множества

# colors = {'red', 'green', 'blue'}
# print(colors)  # {'red', 'green', 'blue'}
# colors.add('red')  # значение не добавится, т.к. оно уже присутствует в этом множестве
# print(colors)  # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors)  # {'red', 'green', 'blue', 'gray'}
# colors.remove('red')  # удалит элемент множества
# print(colors)  # {'green', 'blue', 'gray'}
# colors.remove('red')  # KeyError: 'red'
# colors.discard('red')
# colors.clear()  # очищает множество
# print(colors) # set() - пустой набор

# Операции со множествами в Python

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()             # c = {1, 2, 3, 5, 8}
# u = a.union(b)           # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b)    # i = {8, 2, 5}
# dl = a.difference(b)     # dl = {1, 3}
# dr = b.difference(a)     # dr = {13, 21}
# q = a.union(b).difference(a.intersection(b))  # q = {1, 3, 13, 21}

# Замороженное множество

# a = {1, 8, 6}
#
# b = frozenset(a)
#
# print(b)  # frozenset({8, 1, 6})

# list_1 = [3 for item in range(5)]
# print(list_1)
#
# list_1 = []
#
# for i in range(1, 11):
#     list_1.append(i)
# print(list_1)
#
# list_1 = [i for i in range(1, 11)]
# print(list_1)

list_1 = [i for i in range(1, 11) if i % 4 == 1]
print(list_1)  # Создаст список с четными элементами в указанном диапазоне

list_1 = [(i, i) for i in range(1, 11) if i % 2 == 0]
print(list_1)  # Создаст пару каждому элементу (кортежи)

list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1)  # Также можно умножать, делить, прибавлять, вычитать, Например, умножим на 2