# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# import random
#
# a = int(input("Введите количество элементов первого множества чисел: "))
# b = int(input("Введите количество элементов второго множества чисел: "))
# min_limit = int(input("Введите нижний предел: "))
# max_limit = int(input("Введите верхний предел: "))
# list_a = set([random.randint(min_limit, max_limit) for i in range(a)])
# list_b = set([random.randint(min_limit, max_limit) for j in range(b)])
# print(list_a, list_b)
# result = list_a.intersection(list_b)
# print(sorted(result))

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой
# грядке, причем кусты высажены только по окружности. Таким образом, у каждого
# куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

# import random
#
# a = int(input("Введите количество кустов на грядке: "))
# min_limit = int(input("Введите минимальное количество ягод на одном кусте: "))
# max_limit = int(input("Введите максимальное количество ягод на одном кусте: "))
# current_number_of_berries = 0
# max_of_berries = 0
# bushes = list([random.randint(min_limit, max_limit) for i in range(a)])
# print(bushes)
# for i in range(1, len(bushes) - 1):
#     current_number_of_berries = bushes[i - 1] + bushes[i] + bushes[i + 1]
#     if current_number_of_berries > max_of_berries:
#         max_of_berries = current_number_of_berries
#         print(f"\nmax: {max_of_berries} \nкуст №{i - 1 + 1}, куст №{i + 1}, куст №{i + 1 + 1}", end=" ")
# print(f"\nМаксимальное число ягод, которое собирающий модуль может собрать за один заход: \
# {max_of_berries} ягоду/ягоды/ягод!")

import random

a = int(input("Введите количество кустов на грядке: "))
min_limit = int(input("Введите минимальное количество ягод на одном кусте: "))
max_limit = int(input("Введите максимальное количество ягод на одном кусте: "))
current_number_of_berries = list()
bushes = list([random.randint(min_limit, max_limit) for i in range(a)])
print(bushes)
for i in range(1, len(bushes) - 1):
    current_number_of_berries.append(bushes[i - 1] + bushes[i] + bushes[i + 1])

print(current_number_of_berries)
print(f"\nМаксимальное число ягод, которое собирающий модуль может собрать за один заход: \
{max(current_number_of_berries)} ягоду/ягоды/ягод!")